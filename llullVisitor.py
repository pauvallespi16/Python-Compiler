# Generated from llull.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
else:
    from llullParser import llullParser

# This class defines a complete generic visitor for a parse tree produced by llullParser.

class llullVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by llullParser#root.
    def visitRoot(self, ctx:llullParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#block.
    def visitBlock(self, ctx:llullParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#stat.
    def visitStat(self, ctx:llullParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#function.
    def visitFunction(self, ctx:llullParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#function_stat.
    def visitFunction_stat(self, ctx:llullParser.Function_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#arguments.
    def visitArguments(self, ctx:llullParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#assignment.
    def visitAssignment(self, ctx:llullParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#if_stat.
    def visitIf_stat(self, ctx:llullParser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#condition_block.
    def visitCondition_block(self, ctx:llullParser.Condition_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#stat_block.
    def visitStat_block(self, ctx:llullParser.Stat_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#while_stat.
    def visitWhile_stat(self, ctx:llullParser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#for_stat.
    def visitFor_stat(self, ctx:llullParser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#read.
    def visitRead(self, ctx:llullParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#write.
    def visitWrite(self, ctx:llullParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#array_stat.
    def visitArray_stat(self, ctx:llullParser.Array_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#getter_stat.
    def visitGetter_stat(self, ctx:llullParser.Getter_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#setter_stat.
    def visitSetter_stat(self, ctx:llullParser.Setter_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#expr.
    def visitExpr(self, ctx:llullParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#atom.
    def visitAtom(self, ctx:llullParser.AtomContext):
        return self.visitChildren(ctx)



del llullParser