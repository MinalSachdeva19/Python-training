# While loop:
"""
    while - condition - until condition goes wrong
    While loop is an indefinite loop as the number of iterations in while are not defined .

    Syntax: while condition:
                statement1
                statement2
                statement3
            else:                               (optional statement :will get executed when while condition goes wrong)
                statement4

"""

# While loop considering object as True or False:
num = 3
while num:
    print("This is my while loop!")
    num -= 1
else:
    print("Loop exhausted!")

print("=======================================")

# While loop with break:
num = 3
while num:
    if num == 1:
        break
    print("This is my while loop!")
    num -= 1
else:
    print("Loop exhausted!")

print("=======================================")

# While loop with continue:
num = 3
while num:
    num -= 1
    if num == 2:
        continue
    print("This is my while loop!")
else:
    print("Loop exhausted!")

print("=======================================")

# While loop with condition:
count = 0
while count<3:
    print("Hey!")
    count += 1
else:
    print("Loop exhausted!")

print("=======================================")

# List functions and while loop:
counter = 0
fruits = ["mango", "apple", "kiwi", "papaya"]
while counter<3:
    print(fruits.pop())
    counter +=1
else:
    print("These are all my favourite fruits!")

print("=======================================")

# __iter__ and __next__ function:
l = [1,2,3,4,5]
iterable_obj = iter(l)
print(type(iterable_obj))
print(next(iterable_obj))

print("=======================================")

# Prime numbers:
num = int(input("Enter any number:"))
for i in range(2,num):
    if num%i==0 :
        print("{} is not prime.".format(num))
        break
else:
    print("{} is prime.".format(num))

print("=======================================")

# Prime numbers in some range:
for num in range(1,101):
    for i in range(2,num):
        if num%i==0:
            print("{} is not a Prime number.".format(num))
            break
    else:
        print("{} is prime.".format(num))

# List comprehensions:
"""
    all() : If you pass all True values to me, I will return True.
            If you pass all False values to me, I will return False.
            If you pass even one False value to me, I will return False.
            
    any() : If you give me any True value, I will return True.
            If you give me all False values, I will return False.
            If you give me one False value, even then I will return True.
"""

print("=========================================")

# Prime numbers using list comprehension:
num = int(input("Enter a number:"))
if all([num%i for i in range(2,num)]):
    print("{} is Prime".format(num))
else:
    print("{} is not Prime".format(num))