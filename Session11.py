#Taking input from user:
name = "Minal"
print(f"Entered name is {name}")

name = input("Enter a name :")
print(f"User Entered name is {name}")

name = input("Enter a name:")
age = int(input("Enter age:"))
Location = input("Enter a location:")
print("Hello %s\n\t 1.Age:%d \n\t 2.Location:%s"%(name,age,Location))

#Conditional Statements:
"""
    condition-> True or False
    1. if statement:-
        if condition:
            statement1
            statement2
            statement3
            
    2. if-else statements:-
        if condition:
            statement1
            statement2
            statement3
        else:
            statement4
            statement5
            statement6
            
    3. if-else ladder:-
        if condition:
            statement1
            statement2
            statement3
        elif condition:
            statement4
            statement5
            statement6
        else:
            statement7
            statement8
            statement9
            
    4. nested if-else statements:
        if condition:
            statement1
            if condition:
                sub-statement1
                sub-statement2
            else:
                sub-statement3
                sub-statement4
        else:
            statement2
            statement3
            statement4
"""

#if statement:
a = int(input("Enter a number :"))
if (a>0):
    print("Hello!")

print("-----------------------------------------")

#if-else:
if 0:
    print("It is True")
else:
    print("It is False")

if a%3:
    print("Number is not divisible by 3")
else:
    print("Number is divisible by 3")

print("-----------------------------------------")

#if-else ladder:
num1 = int(input("Enter Number1:"))
num2 = int(input("Enter Number2:"))
if num1>num2:
    print('Number 1 is greater than number 2 ')
elif num2>num1:
    print('Number 2 is greater than number 1 ')
else:
    print("Both the numbers are equal")

print("-----------------------------------------")

#Nested if-else statements:
name = input("Enter a name :")
if name=="Empty":
    print("Container is empty!")
    location = input("Enter a location for container:")
    if location=="Mumbai":
        print("Container Empty found!")
    else:
        print("Container not found in Mumbai.")
else:
    print("Name other than Empty.")