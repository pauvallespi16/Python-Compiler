from antlr4 import *
from beatLexer import beatLexer
from beatParser import beatParser
from EvalVisitor import EvalVisitor
from TreeVisitor import TreeVisitor
input_stream = InputStream(input('? '))
lexer = beatLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = beatParser(token_stream)
tree = parser.root() 
#visitor = TreeVisitor()
#visitor.visit(tree)
visitor = EvalVisitor()
visitor.visit(tree)