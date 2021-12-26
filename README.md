# python-compiler
Compiler for a programming language implemented in Python with the help of the ANTLR tool.
The language instructions are:
 - assignment with =
 - reading with read()
 - write with write()
 - the conditional with if and maybe else
 - iteration with while
 - iteration with for
 - the invocation of a procedure
 - instructions for accessing tables (arrays)

# instructions
To use it, we must invoke Python passing it as the first parameter the file llull.py and as the second parameter the text file with the extension .llull from which we want the code to read. Optionally, we can enter a function name (followed by its parameters if it has one). In this way, we will start the execution with the function entered. If we do not introduce any function, it will start with the function called main. In case there is no main and no function has been passed, the program will return an exception. Also, if a function has been entered that does not exist, the program will return an exception.

