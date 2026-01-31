# Generated from E:/Term7/Compiler/Project/RLangCompiler/grammers/RLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RLangParser import RLangParser
else:
    from RLangParser import RLangParser

# This class defines a complete generic visitor for a parse tree produced by RLangParser.

class RLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RLangParser#prog.
    def visitProg(self, ctx:RLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#environmentDef.
    def visitEnvironmentDef(self, ctx:RLangParser.EnvironmentDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#stateDef.
    def visitStateDef(self, ctx:RLangParser.StateDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#varDecl.
    def visitVarDecl(self, ctx:RLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#ContinuousType.
    def visitContinuousType(self, ctx:RLangParser.ContinuousTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#DiscreteType.
    def visitDiscreteType(self, ctx:RLangParser.DiscreteTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#ContinuousParams.
    def visitContinuousParams(self, ctx:RLangParser.ContinuousParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#DiscreteParams.
    def visitDiscreteParams(self, ctx:RLangParser.DiscreteParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#actionsDef.
    def visitActionsDef(self, ctx:RLangParser.ActionsDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#dynamicsDef.
    def visitDynamicsDef(self, ctx:RLangParser.DynamicsDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#AlwaysRule.
    def visitAlwaysRule(self, ctx:RLangParser.AlwaysRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#WhenRule.
    def visitWhenRule(self, ctx:RLangParser.WhenRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#statementList.
    def visitStatementList(self, ctx:RLangParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#statement.
    def visitStatement(self, ctx:RLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#assignment.
    def visitAssignment(self, ctx:RLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#ifStatement.
    def visitIfStatement(self, ctx:RLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#matchStatement.
    def visitMatchStatement(self, ctx:RLangParser.MatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#matchCase.
    def visitMatchCase(self, ctx:RLangParser.MatchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#rewardsDef.
    def visitRewardsDef(self, ctx:RLangParser.RewardsDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#rewardRule.
    def visitRewardRule(self, ctx:RLangParser.RewardRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#trainingDef.
    def visitTrainingDef(self, ctx:RLangParser.TrainingDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#configAssign.
    def visitConfigAssign(self, ctx:RLangParser.ConfigAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#ActionInListCondition.
    def visitActionInListCondition(self, ctx:RLangParser.ActionInListConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#SimpleCondition.
    def visitSimpleCondition(self, ctx:RLangParser.SimpleConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#IdExpr.
    def visitIdExpr(self, ctx:RLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#NumberExpr.
    def visitNumberExpr(self, ctx:RLangParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#MulDiv.
    def visitMulDiv(self, ctx:RLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#AddSub.
    def visitAddSub(self, ctx:RLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RLangParser#ParenExpr.
    def visitParenExpr(self, ctx:RLangParser.ParenExprContext):
        return self.visitChildren(ctx)



del RLangParser