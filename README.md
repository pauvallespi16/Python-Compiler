# Compiler
Compiler for a programming language implemented in Python with the help of the ANTLR tool.
The language instructions are:
 - assignment with =
 - reading with read()
 - write with write()
 - the conditional with if, else if and maybe else
 - iteration with while
 - iteration with do while
 - iteration with for
 - the invocation of a procedure
 - instructions for accessing tables (arrays)

The available data types are:
 - integers
 - booleans (represented as 0 and 1)
 - arrays

Local and global variables are implemented.

The arithmetic operators are the usual ones (+, -, *, /, %) and with the same priority as in C. Obviously, parentheses can be used. Relational operators (==, <>, <,>, <=,> =) return zero for false and one for true.

It also contains a *pretty-printer* which makes the code more visible and appealing to the user.

# Instructions
First of all you need to install the requirements by using this command:
<pre>python -m pip install -r requirements.txt </pre>

The interpreter is invoked with the command python3 llull.py by passing it as a parameter the name of the file containing the source code (the extension of the files for programs in Llull is .llull). For example:
<pre>python3 llull.py test-file.llull</pre>

You can also call a function of a program directly, by passing the name of the function as a parameter and the values of the parameters of the function, like this:
<pre>python3 llull.py test-file.llull hanoi 1 2 3 4</pre>

The pretty-printer (also called a beautifier because it looks like a beautifier) is invoked with the python3 beat.py command by passing the name of the file containing the source code to beatify as the first parameter. For example:
<pre>python3 beat.py test-file.llull</pre>

### Author
Pau Vallespí Monclús

