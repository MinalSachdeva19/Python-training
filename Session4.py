"""
    2. Comparison Operators: These always return boolean value
        ==  -> equal to
        !=  -> not equal to
        >   -> greater than
        >=  -> greater than equal to
        <   -> lesser than
        <=  -> less than equal to
"""

var = 10
var1 = 24
print(var1==var)
print(var1!=var)
print(var1>var)
print(var1>=var)
print(var1<var)
print(var1<=var)

"""
    3. Assignment Operators:
        += -> increment operator
        -= -> decrement operator
        *= -> multiply assignment operator
        /= -> division assignment operator
        =  -> Assignment operator  (It assigns the value to the identifier)    
"""

var += 1
print(var)
var *= 2
print(var)
var -= 5
print(var)
var /= 2
print(var)

# 4. Is operator: It compares the address of 2 variables .
a = 10
b = 20
print(a is b)
help(print())           # To know the entire documentation of print function .
b = 10
print(a is b)

# id() function:
print(id(a))
print(id(b))

c = 49
print(id(c))
print(a is c)

# isinstance() function: Used to show that eveything in python is an object.
num = 8888
print(type(num))
print(isinstance(num,int))
print(isinstance(12.58,int))
print(isinstance(12.58,float))
print(isinstance(12.58,object))

"""
    5. Bitwise operator: 
        binary(bin), octal(oct), hexadecimal(hex)
        & ->and
        | ->or
        ^ ->XOR
        <<->left shift
        >>->right shift
"""
print(bin(10))
print(oct(20))
print(hex(937))

m = 339
n = 83
print(m&n)
print(m|n)
print(m^n)
print(m<<2)
print(m>>3)

