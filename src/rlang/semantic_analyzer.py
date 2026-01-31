from .generated.RLangVisitor import RLangVisitor
from .generated.RLangParser import RLangParser
from .symbol_table import SymbolTable, Type
from .ir import *

class SemanticAnalyzer(RLangVisitor):
    def __init__(self):
        self.ir = IRModel()
        self.errors = []
        self.symbol_table = SymbolTable()
        self._current_when = None
        self._current_always = None

    # ---------------- STATE ----------------
    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        is_continuous = isinstance(ctx.type_(), RLangParser.ContinuousTypeContext)
        
        domain = []
        if ctx.paramList():
            # Extract parameters
            params = ctx.paramList().expr()
            for p in params:
                domain.append(p.getText())
        
        type_enum = Type.CONTINUOUS if is_continuous else Type.DISCRETE
        
        # 1. Add to Symbol Table
        try:
            self.symbol_table.add(name, type_enum, domain)
        except Exception as e:
            self.errors.append(str(e))
            
        # 2. Add to IR
        self.ir.states[name] = StateIR(name, type_enum, domain)

    # ---------------- ACTIONS ----------------
    def visitActionsDef(self, ctx):
        for idc in ctx.ID():
            action_name = idc.getText()
            self.ir.actions.append(action_name)
            # Add to symbol table
            try:
                self.symbol_table.add_action(action_name)
            except Exception as e:
                self.errors.append(str(e))

    # ---------------- ALWAYS ----------------
    def visitAlwaysRule(self, ctx):
        rule = AlwaysRuleIR()
        self._current_always = rule
        self._current_block = rule.statements  # Start capturing here
        
        self.visitChildren(ctx)
        
        self.ir.always_rules.append(rule)
        self._current_always = None
        self._current_block = None

    # ---------------- WHEN ----------------
    def visitWhenRule(self, ctx):
        cond = ctx.condition()
        if not isinstance(cond, RLangParser.ActionInListConditionContext):
            self.errors.append("semantic error: 'when' only supports 'action in [...]'")
            return

        actions = [e.getText() for e in cond.expr()]
        for act in actions:
            if not self.symbol_table.is_action_defined(act):
               self.errors.append(f"semantic error: Undefined action '{act}' in 'when' clause")

        rule = WhenRuleIR(actions)
        self._current_when = rule
        # When rules currently only support assignments, but we should make it generic if possible
        # For now, let's keep assignment list but also maybe allow block?
        # The IR definition for WhenRuleIR is separate (list of assignments). 
        # For simplicity, I'll stick to assignments for WHEN, but update ALWAYS to use blocks.
        
        self.visitChildren(ctx)
        self.ir.when_rules.append(rule)
        self._current_when = None

    # ---------------- IF STATEMENT ----------------
    def visitIfStatement(self, ctx):
        # Only relevant inside ALWAYS blocks for now
        if not self._current_block is None:
             cond_text = ctx.condition().getText()
             if_ir = IfRuleIR(cond_text, [])
             
             # Push context
             parent_block = self._current_block
             self._current_block = if_ir.statements
             
             # Visit body
             self.visit(ctx.statement())
             
             # Pop context
             self._current_block = parent_block
             
             # Add to parent
             self._current_block.append(if_ir)
        else:
             # If inside WHEN, we ignore IFs or handle them differently?
             # Current IR for WHEN doesn't support nested IFs yet.
             # We let standard traversal happen, but assignments logic needs to know where to go.
             self.visitChildren(ctx)

    # ---------------- MATCH ACTION ----------------
    def visitMatchStatement(self, ctx):
        for case in ctx.matchCase():
            action = case.ID().getText()
            if not self.symbol_table.is_action_defined(action):
                 self.errors.append(f"semantic error: Undefined action '{action}' in match case")

            stmt = case.statement().getChild(0)
            if isinstance(stmt, RLangParser.AssignmentContext):
                assign = AssignmentIR(
                    stmt.ID().getText(),
                    stmt.expr().getText()
                )
                self._validate_assignment(assign)
                if self._current_when:
                    self._current_when.assignments.append(assign)

    # ---------------- ASSIGNMENT ----------------
    def visitAssignment(self, ctx):
        assign = AssignmentIR(
            ctx.ID().getText(),
            ctx.expr().getText()
        )
        self._validate_assignment(assign)
        
        if self._current_block is not None:
            self._current_block.append(assign)
        elif self._current_when:
            self._current_when.assignments.append(assign)
        elif self._current_always:
             # Fallback if block logic fails
             self._current_always.assignments.append(assign)

    def _validate_assignment(self, assign):
        sym = self.symbol_table.get(assign.target)
        if not sym:
            self.errors.append(f"semantic error: Assignment to undefined variable '{assign.target}'")
        elif sym.type == Type.ACTION:
             self.errors.append(f"semantic error: Cannot assign to action '{assign.target}'")

    # ---------------- REWARDS ----------------
    def visitRewardsDef(self, ctx):
        for rule_ctx in ctx.rewardRule():
            cond = rule_ctx.condition().getText()
            rew_expr = rule_ctx.expr().getText()
            self.ir.rewards.append(RewardRuleIR(cond, rew_expr))

    # ---------------- TRAINING ----------------
    def visitTrainingDef(self, ctx):
        for config_ctx in ctx.configAssign():
            key = config_ctx.ID().getText()
            val = config_ctx.expr().getText()
            self.ir.training_config[key] = val

    # ---------------- RUN ----------------
    def analyze(self, tree):
        self._current_block = None
        self.visit(tree)
        return self.ir
