import sys
from antlr4 import *
from llullLexer import llullLexer
from llullParser import llullParser
from BeatVisitor import BeatVisitor

def main(argv):    
    file = open(argv[1])
    input_stream = InputStream(file.read())
    lexer = llullLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = llullParser(token_stream)
    tree = parser.root()
    visitor = BeatVisitor()
    visitor.visit(tree)

if __name__ == '__main__':    
    main(sys.argv)