# Numbers:
"""
    integer = 34 -> int
    float = 364.489 -> float(decimal type value)
    complex = 4+5j -> real+imaginary part
"""
# 1.Arithmetic operators:
a = 50
b = 7
c = 56
print(a+b+c)            # Add operator
print(a-b-c)            # Subtract operator
print(a*b)              # Multiply operator
print(a/b)              # Divide operator
print(a//b)             # Float function -> It will only return the integer part
print(a%c)              # Modulus function -> Returns us with remainder after performing division
print(a**b)             # Power function
print(a**2)             # Square function
print(a**3)             # Cube function

# Multiple ways of printing :
var = 10
s = "Python"
print("Hello")
print('var = {var},{s}')
# First way:
print(f'var = {var}{s}')
print(f'var = {var//2}')        # f for formatting

var1 = 12.6
# Second way:
print('var = %d'%(var))         # %d for integer
print('var1 = %f'%(var1))       # %f for float
print('%d divide by %d = %f'%(25,2,25/2))
print('%d'%(2583.658))
print('Integer values = %d,%d,%d, FLoat values = %.2f,%.2f'%(1,4,5,1445.548,927.6227))

# Third way:
print('var1 is = {}'.format(var))
print('var is = {},{},{},{}'.format(var,30,866.7,"Python"))

# Fourth way:
print('var1 is =',var1)