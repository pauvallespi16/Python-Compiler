if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
    from .llullVisitor import llullVisitor
else:
    from llullParser import llullParser
    from llullVisitor import llullVisitor

class TreeVisitor(llullVisitor):
    def __init__(self):
        self.nivell = 0
    def visitExpr(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            print("  " * self.nivell +
                  llullParser.symbolicNames[l[0].getSymbol().type] +
                  '(' +l[0].getText() + ')')
        else:  # len(l) == 3
            if (l[0].getText() == '('):
                print('  ' *  self.nivell + llullParser.symbolicNames[l[0].getSymbol().type])
                self.nivell += 1
                self.visit(l[1])
                self.nivell -= 1
                print('  ' *  self.nivell + llullParser.symbolicNames[l[2].getSymbol().type])
            else:
                print('  ' *  self.nivell + llullParser.symbolicNames[l[1].getSymbol().type] + '(' + l[1].getText() + ')')
                self.nivell += 1
                self.visit(l[0])
                self.visit(l[2])
                self.nivell -= 1