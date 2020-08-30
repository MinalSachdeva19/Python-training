from MyFirstModule import var
print(var)

print("="*4)

from MyFirstModule import *
# It will import all the methods of paren module but only those which are present in __all__ .
print(add(6,6))
print(var)
print(mul(8,2))
