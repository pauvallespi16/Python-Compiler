if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
    from .llullVisitor import llullVisitor
else:
    from llullParser import llullParser
    from llullVisitor import llullVisitor

memory = {}

global_memory = {}

functions = {}

parameters = {}

aritmetics = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y,
    '^': lambda x,y: x^y,
    '%': lambda x,y: x%y
}

relacionals = {
    '==': lambda x,y: x==y,
    '<>': lambda x,y: x!=y,
    '<=': lambda x,y: x<=y,
    '>=': lambda x,y: x>=y,
    '<': lambda x,y: x<y,
    '>': lambda x,y: x>y
}

# Funcio per a convertir les dades al tipus de dades que requereixi
def autoconvert(s):
    for fn in (int, float):
        try:
            return fn(s)
        except ValueError:
            pass
    return s

def division_by_zero(num):
    # control d'error de divisió entre 0
    if num == 0:
        raise Exception("Division by 0")

def function_redefinition(id):
    # control d'error de redefinició de funcions
    if id in functions:
        raise Exception("Function name is already defined")

def incorrect_parameters(n_params, id):
    # control d'error del número de paràmetres
    if n_params != len(parameters[id]):
        raise Exception("Incorrect number of parameters")

def insufficient_params_write(size):
    # control d'error del write
    if size < 1:
        raise Exception("Write must have at least one argument")

def index_out_of_bounds(pos, size):
    # control d'error d'index fora dels límits
    if pos > size:
        raise Exception("Index out of bounds")

def parameters_out_of_context(param1, param2):
    # control d'error per a les variables locals
    if param1 == None or param2 == None:
        raise Exception("Variables not declared in method")  

def exists_function(function):
    # control d'error per comprovar si existeix una funcio
    if function not in functions:
        raise Exception("Function " + function + " does not exist")  

def exists_variable(var):
    # control d'errors per comprovar si existeix una variable
    l = []
    for elem in parameters.values():
        if elem: l = list(elem.keys())

    if var not in memory and var not in global_memory and var not in l:
        raise Exception("Variable " + var + " does not exist")

class EvalVisitor(llullVisitor):
    def __init__(self, firstFunc, params):
        self.firstFunc = firstFunc
        self.globalVar = False
        self.params = params

    def visitRoot(self, ctx):
        for elem in list(ctx.assignment()):
            self.globalVar = True
            self.visit(elem)
            self.globalVar = False

        for elem in list(ctx.function()):
            self.visit(elem)

        # control d'error
        exists_function('main')

        if self.firstFunc != 'main':
            i = 0
            atrs = parameters[self.firstFunc]
            for elem in atrs:
                parameters[elem] = self.params[i]
                memory[elem] = self.params[i]
                i = i + 1
            
            self.visit(functions[self.firstFunc])
        else: self.visit(functions['main'])
        
    def visitAssignment(self, ctx):
        key = ctx.ID().getText()        # nom variable
        val = self.visit(ctx.expr())    # valor variable
        memory[key] = val

        # afegim a global memory en cas que sigui global
        if self.globalVar == True:
            global_memory[key] = val

    def visitFunction(self, ctx):
        id = ctx.function_stat().ID().getText()
        function_redefinition(id)
        functions[id] = ctx.stat_block()

        # inicialitzem parameters[id] a buit
        parameters[id] = {}
        try:
            atrs = ctx.function_stat().arguments().expr()
            for elem in atrs:
                parameters[id].update({elem.getText(): 0})
                memory[elem.getText()] = 0
        except: pass

    def visitFunction_stat(self, ctx):
        i = 0      # index per iterar sobre la llista
        l = []     # llista on guardem les expressions dels arguments

        if ctx.arguments() != None:
            l = ctx.arguments().expr()

        id = ctx.ID().getText()
        incorrect_parameters(len(l), id)

        aux = memory.copy()   # auxiliar per a poder tornar enrrere a la recursivitat

        # afegim els parametres de la crida a parameters[id]
        for key in parameters[id]:
            parameters[id][key] = self.visit(l[i])
            i = i + 1

        # ens guardem els nous valors a la memòria
        for key in parameters[id]:
            memory[key] = parameters[id][key]

        # borrem tot el que no sigui referent a la crida per a evitar vars. globals
        for key in list(memory):
            if key not in parameters[id] and key not in global_memory:
                memory.pop(key)

        self.visit(functions[ctx.ID().getText()])

        # reomplim el diccionari amb els valors anteriors
        for key in list(aux):
            memory[key] = aux[key]
    
    def visitIf_stat(self, ctx):
        l = list(ctx.condition_block())   # agafa tots els condition_block que conté el context
        evaluatedBlock = False

        # cada 'statement' del if & else if
        for elem in l:
            if self.visit(elem.expr()) == 1:
                evaluatedBlock = True
                self.visit(elem.stat_block())
                break

        if not evaluatedBlock and ctx.stat_block() != None:
            self.visit(ctx.stat_block())

    def visitWhile_stat(self, ctx):
        # mentre es compleixi, seguim en el loop
        while bool(self.visit(ctx.expr())):
            self.visit(ctx.stat_block())

    def visitDo_while_stat(self, ctx):
        # fem una primera iteració
        self.visit(ctx.stat_block())

        # mentre es compleixi, seguim en el loop
        while bool(self.visit(ctx.expr())):
            self.visit(ctx.stat_block())

    def visitFor_stat(self, ctx):
        assigs = list(ctx.assignment())
        self.visit(assigs[0])

        # mentre es compleixi, seguim en el loop
        while bool(self.visit(ctx.expr())):
            self.visit(ctx.stat_block())
            self.visit(assigs[1])

    def visitRead(self, ctx):
        value = autoconvert(input())
        memory[ctx.ID().getText()] = value

    def visitWrite(self, ctx):
        l = list(ctx.expr())
        insufficient_params_write(len(l))

        try: output = str(self.visit(l[0]))
        except: pass

        # per imprimir separat per espais iterem sobre els elements de la llista
        # i els concatenem amb espais
        for i in range (1, len(l)):
            output += ' ' + str(l[i].getText())
            
        print(output)

    def visitArray_stat(self, ctx):
        memory[ctx.ID().getText()] = [0] * self.visit(ctx.expr())

    def visitGetter_stat(self, ctx):
        pos = self.visit(ctx.expr())

        # control d'error
        exists_variable(ctx.ID().getText()) 

        array = memory[ctx.ID().getText()]

        # control d'error
        index_out_of_bounds(pos, len(array))
        return array[pos]

    def visitSetter_stat(self, ctx):
        pos = self.visit(ctx.expr())

        # control d'error
        exists_variable(ctx.ID().getText()) 

        array = memory[ctx.ID().getText()]

        # control d'error
        index_out_of_bounds(pos, len(array))
        array[pos] = self.visit(ctx.atom())

    def visitExpr(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:   # en cas que sigui un atom
            try: return self.visit(ctx.atom()) 
            except: return self.visit(ctx.getter_stat())
        elif len(l) == 2: # en cas que sigui un número negatiu
            return -self.visit(ctx.expr())
        else:
            # parèntesis
            if l[0].getText() == '(' and l[2].getText() == ')':
                self.visit(l[1])
            # operacions
            else:
                parameters_out_of_context(self.visit(l[0]), self.visit(l[2]))
                if l[1].getText() in aritmetics:
                    # control d'error
                    if l[1].getText() == "DIV": division_by_zero(self.visit(l[2]))
                    return aritmetics[l[1].getText()] (self.visit(l[0]), self.visit(l[2]))
                else:  
                    if relacionals[l[1].getText()] (self.visit(l[0]), self.visit(l[2])): return 1
                    else: return 0

    def visitAtom(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 3:
            return self.visit(ctx.expr())
        else:
            # num
            if llullParser.symbolicNames[l[0].getSymbol().type] == 'NUM':
                return int(l[0].getText())
            # string
            elif llullParser.symbolicNames[l[0].getSymbol().type] == 'STRING':
                return l[0].getText().replace('"', '')
            # variable
            else: return memory[l[0].getText()]
