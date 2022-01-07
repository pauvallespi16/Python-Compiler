if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
    from .llullVisitor import llullVisitor
else:
    from llullParser import llullParser
    from llullVisitor import llullVisitor

import colorama
from colorama import Style

"""
    DECISIONS:
        1. Per als números utilitzaré el color TARONJA
        2. Per als strings utilitzaré el color VERD
        3. Per als if / for / while utilitzaré el color VERMELL
        4. Per a void utilitzaré el color VERMELL
        5. Per a declaració de funcions utilitzaré el color LILA
        6. Per a la invocació de funcions utilitzaré el color BLAU
"""

class Style():
    VERMELL = '\033[38;2;255;85;85m'
    BLAU = '\033[38;2;89;196;250m'
    VERD = '\033[38;2;108;255;85m'
    TARONJA = '\033[38;2;255;194;35m'
    RESET = '\033[39m'
    VOID = '\033[38;2;255;85;85m'
    FUNC = '\033[38;2;190;112;244m'

class BeatVisitor(llullVisitor):
    def __init__(self):
        self.spaces = 0

    def visitRoot(self, ctx):
        for elem in list(ctx.assignment()):
            print(self.visit(elem) + '\n')

        l = list(ctx.function())
        for elem in l:
            print(self.visit(elem))
    
    def visitAssignment(self, ctx):
        line = ' ' * self.spaces
        line += Style.RESET + ctx.ID().getText() + Style.RESET + ' = ' + self.visit(ctx.expr()) 
        return line

    def visitFunction(self, ctx):
        l = list(ctx.getChildren())
        line = ' ' * self.spaces
        line += Style.VOID + ctx.VOID().getText() + ' ' + \
            Style.FUNC + ctx.function_stat().ID().getText() + \
            Style.RESET + '('

        # inicialitzem la llista d'arguments buida
        args = []
        size = 0
        try: 
            args = ctx.arguments().expr()
            size = len(args)
        except: pass
        
        if size > 0:
            line += Style.RESET + str(self.visit(args[0]))
            # per a cada argument l'escrivim
            for i in range (1, size):
                line += ', ' + str(self.visit(args[i]))

        line += ') {\n'  
        self.spaces += 4
        line += str(self.visit(ctx.stat_block()))
        self.spaces -= 4
        line += ' ' * self.spaces + Style.RESET + '} \n'
        return line

    def visitFunction_stat(self, ctx):
        line = ' ' * self.spaces
    
        line += Style.BLAU + ctx.ID().getText() + Style.RESET + '('

        # inicialitzem la llista d'arguments buida
        args = []
        size = 0
        try: 
            args = ctx.arguments().expr()
            size = len(args)
        except: pass
        
        if size > 0:
            line += Style.RESET + str(self.visit(args[0]))
            # per a cada argument l'escrivim
            for i in range (1, size):
                line += ', ' + str(self.visit(args[i]))

        line += Style.RESET + ')'  
        return line

    def visitRead(self, ctx):
        line = ' ' * self.spaces

        # escrivim el read i els parèntesis
        line += Style.BLAU + ctx.READ().getText() + Style.RESET + '(' + \
            Style.RESET + ctx.ID().getText() + Style.RESET + ')'
        return line

    def visitWrite(self, ctx):
        line = ' ' * self.spaces
        line += Style.BLAU + ctx.WRITE().getText() + Style.RESET + '('
        args = ctx.expr()
        size = len(args)
    
        # escrivim els arguments
        if (size > 0):
            line += Style.RESET + str(self.visit(args[0]))
            # per a cada argument l'escrivim
            for i in range (1, size):
                line += ', ' + str(self.visit(args[i]))

        line += Style.RESET + ')'
        return line

    def visitStat_block(self, ctx):        
        return self.visit(ctx.block())
        
    def visitBlock(self, ctx):
        l = ctx.getChildren()
        line = ''
        for elem in l:
            line += str(self.visit(elem)) + '\n'
        return line

    def visitIf_stat(self, ctx):
        conds = list(ctx.condition_block())
        line = ' ' * self.spaces

        # escrivim el if i els else if en cas que hi hagi
        for i in range (0, len(conds)):
            if i == 0: line += Style.VERMELL + 'if '
            else:  line += Style.VERMELL + ' ' * self.spaces + 'else if '
            line += Style.RESET + '('
            aux = self.spaces
            self.spaces = 0  # això ho faig per a evitar que al visitar l'expr hi hagi més espais del compte
            line += self.visit(conds[0].expr())
            line += Style.RESET + ') ' + '{\n'
            self.spaces += aux + 4
            line += str(self.visit(conds[0].stat_block()))
            self.spaces -= 4
            line += ' ' * self.spaces + Style.RESET + '}'
            if i != len(conds)-1: line += '\n'   
        
        # en cas que hi hagi else
        if ctx.stat_block() != None:
            line += '\n' + ' ' * self.spaces + Style.VERMELL + 'else ' + \
                Style.RESET + '{\n'
            self.spaces += 4
            line += str(self.visit(ctx.stat_block()))
            self.spaces -= 4
            line += ' ' * self.spaces + Style.RESET + '}'


        return line

    def visitWhile_stat(self, ctx):
        l = list(ctx.getChildren())
        line = ' ' * self.spaces

        # escrivim el while i l'expressió
        line += Style.VERMELL + ctx.WHILE().getText() + \
                Style.RESET + ' (' + self.visit(ctx.expr()) + \
                Style.RESET + ') {\n'
        self.spaces += 4
        line += self.visit(ctx.stat_block())
        self.spaces -= 4
        line += ' ' * self.spaces + Style.RESET + '}' 
        return line

    def visitDo_while_stat(self, ctx):
        l = list(ctx.getChildren())
        line = ' ' * self.spaces
        
        # escrivim el do
        line += Style.VERMELL + ctx.DO().getText() + Style.RESET + ' { \n'
        self.spaces += 4
        line += self.visit(ctx.stat_block())
        self.spaces -= 4

        # mateix procediment que amb el while
        line += ' ' * self.spaces + Style.RESET + '} ' + Style.VERMELL + ctx.WHILE().getText() + \
                Style.RESET + ' (' + self.visit(ctx.expr()) + \
                Style.RESET + ')'
   
        return line

    def visitFor_stat(self, ctx):
        assigs = list(ctx.assignment())
        line = ' ' * self.spaces

        # escrivim el for
        line += Style.VERMELL + ctx.FOR().getText() + \
            Style.RESET + ' ('

        # pel mateix motiu que abans, posem els espais a 0
        aux = self.spaces
        self.spaces = 0
        line += self.visit(assigs[0]) + Style.RESET + '; ' + \
            self.visit(ctx.expr()) + '; ' + Style.RESET + self.visit(assigs[1]) + \
            Style.RESET + ') {\n'
        
        # tornem a guardar els espais d'abans
        self.spaces = aux
        self.spaces += 4
        
        line += self.visit(ctx.stat_block())
        self.spaces -= 4
        line += ' ' * self.spaces + Style.RESET + '}' 
        return line
        
    def visitArray_stat(self, ctx):
        line = ' ' * self.spaces
        
        # escrivim array i l'expressió
        line += Style.BLAU + ctx.ARRAY().getText() + Style.RESET + '(' + Style.RESET + \
            ctx.ID().getText() + Style.RESET + ', ' + str(self.visit(ctx.expr())) + Style.RESET + ')'
        return line
    
    def visitGetter_stat(self, ctx):
        line = ' ' * self.spaces

        # escrivim get i l'expressió
        line += Style.BLAU + ctx.GET().getText() + Style.RESET + '(' + \
            Style.RESET + ctx.ID().getText() + Style.RESET + ', ' + str(self.visit(ctx.expr())) + Style.RESET + ')'
        return line   
    
    def visitSetter_stat(self, ctx):
        line = ' ' * self.spaces

        # escrivim set i l'expressió
        line += Style.BLAU + ctx.SET().getText() + Style.RESET + '(' + \
            Style.RESET + ctx.ID().getText() + Style.RESET + ', ' + str(self.visit(ctx.expr())) + \
            Style.RESET + ', ' + str(self.visit(ctx.atom())) + Style.RESET + ')'
        return line

    def visitExpr(self, ctx):
        l = list(ctx.getChildren())
        line = ''
        if len(l) == 1:   # en cas que sigui un atom
            try: line += self.visit(ctx.atom()) 
            except: line += self.visit(ctx.getter_stat())
        elif len(l) == 2: # en cas que sigui un número negatiu
            line += '-' + str(self.visit(ctx.expr()))
        else: 
            # parèntesis
            if l[0].getText() == '(' and l[2].getText() == ')':
                line += '(' + self.visit(l[1]) + ')'
            # operacions
            else:
                line += self.visit(l[0]) + \
                    ' ' + Style.RESET + l[1].getText() + ' ' + \
                    self.visit(l[2])
        return line

    def visitAtom(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 3:
            return self.visit(ctx.expr())
        else:
            # num o bool
            if llullParser.symbolicNames[l[0].getSymbol().type] == ('NUM' or 'TRUE' or 'FALSE'):
                return Style.TARONJA + l[0].getText()
            # string
            elif llullParser.symbolicNames[l[0].getSymbol().type] == 'STRING':
                return Style.VERD + l[0].getText()
            # variable
            else: return Style.RESET + l[0].getText();