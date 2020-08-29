# Exception Handling: Handling errors that occured at run time.
# 1. Zero Division error:
print("1. Zero Division Error:")

try:
    number = int(input("Enter any number:"))
    print("20 divided by {} = {}".format(number,20/number))
except ZeroDivisionError as Z:
    print("Division by zero is not valid, error:", Z)

# 2. Name Error:
print("2. Name Error:")
try:
    number = int(input("Enter any number:"))
    print("20 divided by {} = {}".format(numbers,20/number))
except ZeroDivisionError as Z:
    print("Division by zero is not valid, error:", Z)
except NameError as N:
    print("Identifier name of integer is having some problem in initialization.")

print("="*68)

# Nested try-except:
try:
    number = int(input("Enter any number:"))
    print("20 divided by {} = {}".format(number,20/number))
except ZeroDivisionError as Z:
    print("Division by zero is not valid, error:", Z)
    try:
        number = int(input("Enter the number again:"))
        print("20 divided by {} = {}".format(number, 20 / number))
    except ZeroDivisionError as Z:
        print("Division by zero is not valid and you are again entering a worong input, Error:", Z)
except NameError as N:
    print("Identifier name of integer is having some problem in initialization.")

print("="*68)

# Try-except with loops:
counter = 0

while counter<3:
    try:
        number = int(input("Enter any number:"))
        print("20 divided by {} = {}".format(number, 20 / number))
    except ZeroDivisionError as Z:
        print("Division by zero is not valid, error:", Z)
    counter += 1

print("="*68)

# Try-except-else-finally:
try:
    number = int(input("Enter any number:"))
    print("20 divided by {} = {}".format(number,20/number))
except ZeroDivisionError as Z:
    print("Division by zero is not valid, error:", Z)
except NameError as N:
    print("Identifier name of integer is having some problem in initialization.")
else:
    print("No exception in try block!")
finally:
    print("Stop me if you can!!!")

print("="*68)

# Finally and exit: else will not get executed but finally will get executed as nothing can stop finally except killing a process.
try:
    number = int(input("Enter any number:"))
    print("20 divided by {} = {}".format(number,20/number))
    exit()
except ZeroDivisionError as Z:
    print("Division by zero is not valid, error:", Z)
except NameError as N:
    print("Identifier name of integer is having some problem in initialization.")
else:
    print("No exception in try block!")
finally:
    print("Stop me if you can!!!")

print("="*68)

# Exception class:
try:
    number = int(input("Enter any number:"))
    print("20 divided by {} = {}".format(number,20/number))
except Exception as E:
    print("Division operation is having issue!, Error:", E)

print("="*68)

# System module:
import sys

try:
    number = int(input("Enter any number:"))
    print("20 divided by {} = {}".format(number, 20 / number))
except Exception as E:
    print("Division operation is having issue!, Error:", sys.exc_info())
    print("Division operation is having issue!, Error:", sys.exc_info()[0])
    print("Division operation is having issue!, Error:", sys.exc_info()[1])

print("="*68)

# User defined exceptions: Raise function
share = input("Please enter the share you want o buy/sell:")
quantity = int(input("Please enter number of share you want to buy/sell:"))
if quantity==0 or quantity>10000:
    print("You are entering a wrong input.")
else:
    print("Shares are yours!")

print("-"*68)

# Raise function:
share = input("Please enter the share you want o buy/sell:")
quantity = int(input("Please enter number of share you want to buy/sell:"))
if quantity==0 or quantity>10000:
    raise ValueError("You cannot buy zero share or more han 10000 shares!")
else:
    print("Shares are yours!")

