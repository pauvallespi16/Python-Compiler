import sys
from antlr4 import *
from llullLexer import llullLexer
from llullParser import llullParser
from EvalVisitor import EvalVisitor
from TreeVisitor import TreeVisitor

def main(argv):    
    file = open(argv[1])
    function = 'main'
    if len(argv) > 2:
        function = argv[2]
    params = []
    for i in range(3, len(sys.argv)):
        elem = sys.argv[i]
        if (elem.isnumeric()): params.append(int(elem))
        else: params.append(elem)

    input_stream = InputStream(file.read())
    lexer = llullLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = llullParser(token_stream)
    tree = parser.root()
    visitor = EvalVisitor(function, params)
    visitor.visit(tree)

if __name__ == '__main__':    
    main(sys.argv)