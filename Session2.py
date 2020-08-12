"""
    Python was implemented using c Language.
    compiler -> python file(.py) -> .pyc compiled python file -> interpreter
    Python is both compiler and interpreter based language. But if one is to be choosen, interpreted
    one will be choosen as the last step is to approach interpreter.

    Difference between python version 2 and version 3 :
    Python 2 uses print as a statement which is simply written in single or double quotes.
    Python 3  uses print as a functio which is written in open and closed parantheses and
    closing of parantheses indicates end of the function . Indexing is taken care of .
    We cannot run python 3 in Python 2 and vice versa.

    Comments : Single-line comments are created simply by beginning a line with the hash (#) character,
    and they are automatically terminated by the end of line. Comments that span multiple
    lines – used to explain things in more detail – are created by adding a delimiter (“””) on each
    end of the comment.

    Identifier : It is the name used to identify variables, functions, class, module or other objects.
    (start identifier with a-z, A-Z,
    identifiers can contain 0-9)
"""

# Variables :
x = 5
y = 10
print(x)
print(y)

# Python is a case sensitive language :
var1 = 30
Var1 = 40
print(var1)
print(Var1)

"""
    Data types : Data type is an important concept.
    Variables can store data of different types, and different types can do different things.
    Built-in data types:
    1.Text type : str
    2.Numeric types : int, float, complex
    3.Sequence type : list, tuple, range
    4.Mapping type :  dict (key:value)
    5.Set type :      set
    6.Boolean :       bool (true/False)
    Binary type :     bytes, bytearray
"""

# Numbers :
a = 2
b = 2.579
c = 3+4i
print(type(a))
print(type(b))
print(type(c))

# Strings :
print(type("I am doing good today"))
print("I'm doing good today")
#If your string have single inverted commas ,use double one to write entire string and vice versa.
#print('I'm doing good today)





