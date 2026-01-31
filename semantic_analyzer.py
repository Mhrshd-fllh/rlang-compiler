from generated.RLangVisitor import RLangVisitor
from generated.RLangParser import RLangParser
from symbol_table import Type
from ir import *

class SemanticAnalyzer(RLangVisitor):
    def __init__(self):
        self.ir = IRModel()
        self.errors = []
        self._current_when = None
        self._current_always = None

    # ---------------- STATE ----------------
    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        if isinstance(ctx.type_(), RLangParser.ContinuousTypeContext):
            self.ir.states[name] = Type.CONTINUOUS
        else:
            self.ir.states[name] = Type.DISCRETE

    # ---------------- ACTIONS ----------------
    def visitActionsDef(self, ctx):
        for idc in ctx.ID():
            self.ir.actions.append(idc.getText())

    # ---------------- ALWAYS ----------------
    def visitAlwaysRule(self, ctx):
        rule = AlwaysRuleIR()
        self._current_always = rule
        self.visitChildren(ctx)
        self.ir.always_rules.append(rule)
        self._current_always = None

    # ---------------- WHEN ----------------
    def visitWhenRule(self, ctx):
        cond = ctx.condition()
        if not isinstance(cond, RLangParser.ActionInListConditionContext):
            self.errors.append("when فقط action in [...] را پشتیبانی می‌کند")
            return

        actions = [e.getText() for e in cond.expr()]
        rule = WhenRuleIR(actions)
        self._current_when = rule
        self.visitChildren(ctx)
        self.ir.when_rules.append(rule)
        self._current_when = None

    # ---------------- MATCH ACTION ----------------
    def visitMatchStatement(self, ctx):
        for case in ctx.matchCase():
            action = case.ID().getText()
            stmt = case.statement().getChild(0)
            if isinstance(stmt, RLangParser.AssignmentContext):
                assign = AssignmentIR(
                    stmt.ID().getText(),
                    stmt.expr().getText()
                )
                self._current_when.assignments.append(assign)

    # ---------------- ASSIGNMENT ----------------
    def visitAssignment(self, ctx):
        assign = AssignmentIR(
            ctx.ID().getText(),
            ctx.expr().getText()
        )
        if self._current_always:
            self._current_always.assignments.append(assign)

    # ---------------- RUN ----------------
    def analyze(self, tree):
        self.visit(tree)
        return self.ir
