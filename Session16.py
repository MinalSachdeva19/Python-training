# applepie -> to simply print the index:
"""
    expected output:
        a - [0]
        p - [1]
        p - [2]
        l - [3]
        e - [4]
        p - [5]
        i - [6]
        e - [7]

"""

input = "applepie"
for i in range(len(input)):
    print("{} - [{}]".format(input[i], i))

print("="*40)

# Object Oriented Programming:
"""
    class -> attributes and functionalities
    Functions : user defined functions
                    def fnc_name(args):                 # Function definition
                        indentation starts
                        statement 1
                        statement 2
                        statement 3
                        
                    fnc_name(args)                      # Function call
                    
"""

# User defined function without arguments:
def first_function():
    print("This function is created by me!")
    if True:
        print("True")
    else:
        print("False")
    for i in "Minal":
        print(i)
print("Look at the following statements:")
first_function()

print("="*40)

# User defined functions with arguments:
def first_function(args):
    args += 2
    print( "Argument is:",args)
    print("This function is created by me!")
    if True:
        print("True")
    else:
        print("False")
    for i in "Minal":
        print(i)
print("Look at the following statements:")
var = 45
print( "var is:",var)
first_function(var)
print(var)

print("="*40)

# Directly passing arguments:

def first_function(args):
    args += 2
    print( "Argument is:",args)
    print("This function is created by me!")
    if True:
        print("True")
    else:
        print("False")
    for i in "Minal":
        print(i)
print("Look at the following statements:")
var = 45
print( "var is:",var)
first_function(14)
print( "var is:",var)

"""
    Types of arguments:
        1. Positional arguments : The type in which we directly pass value or objects to the function while calling.
                                  The first value maps the first identifier of the function in definition, second one 
                                  maps the second and so on.
        2. Keyword arguments    : When we call a function with some values, these values get assigned to the arguments
                                  according to their postion.
        3. Default arguments    : By providing default valueto an argument by using the assignment(=) operator.
        4. Non default arguments: Those arguments to which we don't pass any value in function definition.
        
"""

print("="*60)

# Positional Arguments :
def function(a,b,c,d):
    print(a*b+c*d)
    print("This is my multiplication and addition expression.")
    if a*b>c*d:
        print("First sub expression is greater.")
    else:
        print("Second sub expression is greater.")
print("Let's look what happens!")
function(34,464,676,78)
print("Great!")

print("="*60)

# Keyword arguments:
def function(a,b,c,d):
    print(a*b+c*d)
    print("This is my multiplication and addition expression.")
    if a*b>c*d:
        print("First sub expression is greater.")
    else:
        print("Second sub expression is greater.")
print("Let's look what happens!")
function(c=97,a=464,d=676,b=7978)
print("Great!")

print("="*60)

# Default and non default arguments :
def add(a,b=86):                # "a" is non default argument.
    print(a+b)

a= 26
b= 3
add(a)              # Will pick the default value of "b" i.e. 86.
add(a,b)            # Will overwrite the value of b=86 to b=3.
add(b)              # Will simply revert back with default value of "b".
