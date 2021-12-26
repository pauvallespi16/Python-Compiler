grammar llull;

root: function* EOF ;

block: stat* ;

stat: assignment
    | array_stat
    | getter_stat
    | setter_stat
    | if_stat
    | while_stat
    | for_stat
    | function_stat
    | read
    | write
    ;

function: VOID function_stat stat_block;

function_stat: ID PARL arguments? PARR;

arguments: expr (COMMA expr)*;

assignment: ID ASSIG expr;

if_stat: IF condition_block (ELSE IF condition_block)* (ELSE stat_block)?;

condition_block: expr stat_block;

stat_block: BRACEL block BRACER;

while_stat: WHILE expr stat_block;

for_stat: FOR PARL assignment SCOL expr SCOL assignment PARR stat_block;

read: READ PARL ID PARR;

write: WRITE PARL expr (COMMA expr)* PARR;

array_stat: ARRAY PARL ID COMMA expr PARR;

getter_stat: GET PARL ID COMMA expr PARR;

setter_stat: SET PARL ID COMMA expr COMMA atom PARR;

expr: getter_stat
    | <assoc=right> expr POW expr 
    | SUB expr       // nombres negatius
    | expr (MULT | DIV | MOD) expr
    | expr (ADD | SUB | GT | LT | GT_EQ | LT_EQ | EQUAL | NOT_EQ) expr
    | atom
    ;

atom: PARL expr PARR  // parèntesis
    | NUM             // número
    | (TRUE | FALSE)  // booleà
    | STRING          // string
    | ID              // variables
    ;

// Nombres
NUM     : [0-9]+;

// Parentesis
PARL    : '(' ;
PARR    : ')' ;
BRACEL  : '{' ;
BRACER  : '}' ;

// Operadors aritmetics
ADD     : '+' ;
SUB     : '-' ;
MULT    : '*' ;
DIV     : '/' ;
POW     : '^' ;
MOD     : '%' ;

// Operadors racionals
GT      : '>' ;
LT      : '<' ;
GT_EQ   : '>=';
LT_EQ   : '<=';
EQUAL   : '==';
NOT_EQ  : '<>';

// Instruccions
READ    : 'read';
WRITE   : 'write';
IF      : 'if';
WHILE   : 'while';
FOR     : 'for';
ELSE    : 'else';
VOID    : 'void';
ARRAY   : 'array';
GET     : 'get';
SET     : 'set';

// Altres
COMMA   : ',';
SCOL    : ';';
ASSIG   : '=' ;
ZERO    : '0' ;
TRUE    : 'true';
FALSE   : 'false';
STRING  : '"' (~["\r\n] | '""')* '"';

// Variables
ID     : [a-zA-Z] [a-zA-Z_0-9]*;

// Comentaris
COMMENT : '#' ~[\r\n]* -> skip;

WS : [ \n]+ -> skip ;
