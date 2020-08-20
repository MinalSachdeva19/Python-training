# Rules for arguments:
"""
    Rule 1: While defining or calling the function, positional arguments should not follow keyword arguments .
    Rule 2: One positional argument should not have multiple values.
    Rule 3: Non-default argument should not follow default argument. Once a default argument is encountered,
            all the arguments should be default then.

"""

def add(a,b=63):
    print("Addition of numbers is:")
    return a+b
print(add(2,43))
print(add(23))
print(add(a=57,b=87))
print(add(50,50))

print("==============================================================")

# Default "b", non default "c" -> non-default argument follows default argument :
# def function(a,b=845,c,d=784):
#     print(a*b+c*d)
#     print("This is my multiplication and addition expression.")
#     if a*b>c*d:
#         print("First sub expression is greater.")
#     else:
#         print("Second sub expression is greater.")
# print("Let's look what happens!")
# a = 29
# b = 40
# c = 74
# d = 47
# function(a,c)
# print("Great!")

print("==============================================================")


# Default "b", making "c" default
def function(a,b=45,c=8,d=4):
    print("This is my result for the expression:")
    print(a * b + c * d)
print("Let's look what happens!")
a = 29
b = 40
c = 74
d = 47
function(20,25)
function(87)

print("==============================================================")

# Default "b", making "c" to not follow default argument :
def add(a,c,b=63):
    print("Addition of numbers is:")
    return a+b+c
print(add(2,43))
print(add(23,12))
print(add(a=57,b=87,c=20))
print(add(50,50))
#print(add(b=100,87,57))               # Will return error -> positional argument follows keyword argument

# Unlimited Positional and keyword arguments:
"""
    Positional: *args
    Keyword:    **kwargs
"""

print("==============================================================")

def add(*args):
    print(args)
    print(type(args))
    num_sum = 0
    print("Result is:")
    for num in args:
        num_sum += num
    return num_sum
print(add(8,2,4,6,8,0,67,44))

print("==============================================================")

def function(**kwargs):
    print(kwargs)
    print(type(kwargs))
print(function(a=98,b=3,c=5))

# Output is displaying None. Why?
# {'a': 98, 'b': 3, 'c': 5}
# <class 'dict'>
# None

print("==============================================================")

def combination(*args,**kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
print(combination(1,3,5,6,8,9,0,56,6,a=98,b=3,c=5))

print("==============================================================")

def square(num):
    return num**2
def cube(num):
    return num**3
def result(num):
    print("square of {} = {}".format(num,square(num)))
    print("cube of {} = {}".format(num, cube(num)))
result(34)
print("-"*40)
result(int(input("Enter any number from 1-100:")))

print("==============================================================")

# Map Function:
def cube(num):
    return num**3
for i in range(1,11):
    print(cube(i))

print("-"*40)

# Instead of writing for loop, we can use map function:
def cube(num):
    return num**3
print(map(cube,range(1,11)))
print(list(map(cube,range(1,11))))

print("-"*40)

def cube(num):
    print("Value of argument passed is:",num)
    return num**3
print(map(cube,range(1,11)))
print(list(map(cube,range(1,11))))

print("-"*40)

def function(num):
    print("Value of argument passed is:",num)
    return num
print(map(function,range(1,11)))
print(list(map(function,range(1,11))))

print("-"*40)

def function(num):
    print("Value of argument passed is:",num)
    return 234                                      # Map will return 234 every time function is called.
print(map(function,range(1,11)))
print(list(map(function,range(1,11))))

print("==============================================================")

# Filter function: Returns the original value. Will return true values always.
def function(num):
    print("Value of argument passed is:",num)
    return num
print(filter(function,range(1,11)))
print(list(filter(function,range(1,11))))

print("-"*40)

def function(num):
    print("Value of argument passed is:",num)
    return 12
print(filter(function,range(1,11)))
print(list(filter(function,range(1,11))))

"""
    Map takes all objects in a list and allows you to apply a function to it whereas 
    Filter takes all objects in a list and runs that through a function to create a new 
    list with all objects that return True in that function.
"""

def function(var):
    if var%2==0:
        return True
    else:
        return False
print(list(filter(function,range(1,6))))

print("-"*40)

def function(var):
    if var%2==0:
        return True
    else:
        return False
print(list(map(function,range(1,6))))
