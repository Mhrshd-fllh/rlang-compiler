# Generated from E:/Term7/Compiler/Project/RLangCompiler/grammers/RLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RLangParser import RLangParser
else:
    from RLangParser import RLangParser

# This class defines a complete listener for a parse tree produced by RLangParser.
class RLangListener(ParseTreeListener):

    # Enter a parse tree produced by RLangParser#prog.
    def enterProg(self, ctx:RLangParser.ProgContext):
        pass

    # Exit a parse tree produced by RLangParser#prog.
    def exitProg(self, ctx:RLangParser.ProgContext):
        pass


    # Enter a parse tree produced by RLangParser#environmentDef.
    def enterEnvironmentDef(self, ctx:RLangParser.EnvironmentDefContext):
        pass

    # Exit a parse tree produced by RLangParser#environmentDef.
    def exitEnvironmentDef(self, ctx:RLangParser.EnvironmentDefContext):
        pass


    # Enter a parse tree produced by RLangParser#stateDef.
    def enterStateDef(self, ctx:RLangParser.StateDefContext):
        pass

    # Exit a parse tree produced by RLangParser#stateDef.
    def exitStateDef(self, ctx:RLangParser.StateDefContext):
        pass


    # Enter a parse tree produced by RLangParser#varDecl.
    def enterVarDecl(self, ctx:RLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by RLangParser#varDecl.
    def exitVarDecl(self, ctx:RLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by RLangParser#ContinuousType.
    def enterContinuousType(self, ctx:RLangParser.ContinuousTypeContext):
        pass

    # Exit a parse tree produced by RLangParser#ContinuousType.
    def exitContinuousType(self, ctx:RLangParser.ContinuousTypeContext):
        pass


    # Enter a parse tree produced by RLangParser#DiscreteType.
    def enterDiscreteType(self, ctx:RLangParser.DiscreteTypeContext):
        pass

    # Exit a parse tree produced by RLangParser#DiscreteType.
    def exitDiscreteType(self, ctx:RLangParser.DiscreteTypeContext):
        pass


    # Enter a parse tree produced by RLangParser#ContinuousParams.
    def enterContinuousParams(self, ctx:RLangParser.ContinuousParamsContext):
        pass

    # Exit a parse tree produced by RLangParser#ContinuousParams.
    def exitContinuousParams(self, ctx:RLangParser.ContinuousParamsContext):
        pass


    # Enter a parse tree produced by RLangParser#DiscreteParams.
    def enterDiscreteParams(self, ctx:RLangParser.DiscreteParamsContext):
        pass

    # Exit a parse tree produced by RLangParser#DiscreteParams.
    def exitDiscreteParams(self, ctx:RLangParser.DiscreteParamsContext):
        pass


    # Enter a parse tree produced by RLangParser#actionsDef.
    def enterActionsDef(self, ctx:RLangParser.ActionsDefContext):
        pass

    # Exit a parse tree produced by RLangParser#actionsDef.
    def exitActionsDef(self, ctx:RLangParser.ActionsDefContext):
        pass


    # Enter a parse tree produced by RLangParser#dynamicsDef.
    def enterDynamicsDef(self, ctx:RLangParser.DynamicsDefContext):
        pass

    # Exit a parse tree produced by RLangParser#dynamicsDef.
    def exitDynamicsDef(self, ctx:RLangParser.DynamicsDefContext):
        pass


    # Enter a parse tree produced by RLangParser#AlwaysRule.
    def enterAlwaysRule(self, ctx:RLangParser.AlwaysRuleContext):
        pass

    # Exit a parse tree produced by RLangParser#AlwaysRule.
    def exitAlwaysRule(self, ctx:RLangParser.AlwaysRuleContext):
        pass


    # Enter a parse tree produced by RLangParser#WhenRule.
    def enterWhenRule(self, ctx:RLangParser.WhenRuleContext):
        pass

    # Exit a parse tree produced by RLangParser#WhenRule.
    def exitWhenRule(self, ctx:RLangParser.WhenRuleContext):
        pass


    # Enter a parse tree produced by RLangParser#statementList.
    def enterStatementList(self, ctx:RLangParser.StatementListContext):
        pass

    # Exit a parse tree produced by RLangParser#statementList.
    def exitStatementList(self, ctx:RLangParser.StatementListContext):
        pass


    # Enter a parse tree produced by RLangParser#statement.
    def enterStatement(self, ctx:RLangParser.StatementContext):
        pass

    # Exit a parse tree produced by RLangParser#statement.
    def exitStatement(self, ctx:RLangParser.StatementContext):
        pass


    # Enter a parse tree produced by RLangParser#assignment.
    def enterAssignment(self, ctx:RLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by RLangParser#assignment.
    def exitAssignment(self, ctx:RLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by RLangParser#ifStatement.
    def enterIfStatement(self, ctx:RLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by RLangParser#ifStatement.
    def exitIfStatement(self, ctx:RLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by RLangParser#matchStatement.
    def enterMatchStatement(self, ctx:RLangParser.MatchStatementContext):
        pass

    # Exit a parse tree produced by RLangParser#matchStatement.
    def exitMatchStatement(self, ctx:RLangParser.MatchStatementContext):
        pass


    # Enter a parse tree produced by RLangParser#matchCase.
    def enterMatchCase(self, ctx:RLangParser.MatchCaseContext):
        pass

    # Exit a parse tree produced by RLangParser#matchCase.
    def exitMatchCase(self, ctx:RLangParser.MatchCaseContext):
        pass


    # Enter a parse tree produced by RLangParser#rewardsDef.
    def enterRewardsDef(self, ctx:RLangParser.RewardsDefContext):
        pass

    # Exit a parse tree produced by RLangParser#rewardsDef.
    def exitRewardsDef(self, ctx:RLangParser.RewardsDefContext):
        pass


    # Enter a parse tree produced by RLangParser#rewardRule.
    def enterRewardRule(self, ctx:RLangParser.RewardRuleContext):
        pass

    # Exit a parse tree produced by RLangParser#rewardRule.
    def exitRewardRule(self, ctx:RLangParser.RewardRuleContext):
        pass


    # Enter a parse tree produced by RLangParser#trainingDef.
    def enterTrainingDef(self, ctx:RLangParser.TrainingDefContext):
        pass

    # Exit a parse tree produced by RLangParser#trainingDef.
    def exitTrainingDef(self, ctx:RLangParser.TrainingDefContext):
        pass


    # Enter a parse tree produced by RLangParser#configAssign.
    def enterConfigAssign(self, ctx:RLangParser.ConfigAssignContext):
        pass

    # Exit a parse tree produced by RLangParser#configAssign.
    def exitConfigAssign(self, ctx:RLangParser.ConfigAssignContext):
        pass


    # Enter a parse tree produced by RLangParser#ActionInListCondition.
    def enterActionInListCondition(self, ctx:RLangParser.ActionInListConditionContext):
        pass

    # Exit a parse tree produced by RLangParser#ActionInListCondition.
    def exitActionInListCondition(self, ctx:RLangParser.ActionInListConditionContext):
        pass


    # Enter a parse tree produced by RLangParser#SimpleCondition.
    def enterSimpleCondition(self, ctx:RLangParser.SimpleConditionContext):
        pass

    # Exit a parse tree produced by RLangParser#SimpleCondition.
    def exitSimpleCondition(self, ctx:RLangParser.SimpleConditionContext):
        pass


    # Enter a parse tree produced by RLangParser#IdExpr.
    def enterIdExpr(self, ctx:RLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by RLangParser#IdExpr.
    def exitIdExpr(self, ctx:RLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by RLangParser#NumberExpr.
    def enterNumberExpr(self, ctx:RLangParser.NumberExprContext):
        pass

    # Exit a parse tree produced by RLangParser#NumberExpr.
    def exitNumberExpr(self, ctx:RLangParser.NumberExprContext):
        pass


    # Enter a parse tree produced by RLangParser#MulDiv.
    def enterMulDiv(self, ctx:RLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by RLangParser#MulDiv.
    def exitMulDiv(self, ctx:RLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by RLangParser#AddSub.
    def enterAddSub(self, ctx:RLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by RLangParser#AddSub.
    def exitAddSub(self, ctx:RLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by RLangParser#ParenExpr.
    def enterParenExpr(self, ctx:RLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by RLangParser#ParenExpr.
    def exitParenExpr(self, ctx:RLangParser.ParenExprContext):
        pass



del RLangParser