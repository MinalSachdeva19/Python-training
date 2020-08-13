# Nested for loop:
var = ["var1", "var2", "var3", "var4"]
for i in var:
    for m in var:
        print(i,m)

#Printing all the natural numbers:
num = int(input("Enter any number:"))
sum_num = 0 
for i in range(1,num+1):
    if i<=5:
        sum_num += i
print(sum_num)

#Printing all the odd numbers:
num = int(input("Enter any number:"))
sum_num = 0
for i in range(1,num+1):
    if i%2:
        sum_num += i
print(sum_num)

#Printing all the even numbers:
num = int(input("Enter any number:"))
sum_num = 0
for i in range(1,num+1):
    if i%2==0:
        sum_num += i
print(sum_num)

print("====================================")

# Continue keyword: The continue statement in Python returns the control to the beginning of the for loop.
# The continue statement rejects all the remaining statements in the current iteration of the loop and moves the
# control back to the top of the loop. The continue statement can be used in both while and for loops.
for i in range(1,11):
    if i == 5:
        continue
    else:
        print(i)

print(" ")

for i in "Python":
    if i == "y":
        continue
    print("value is: ",i)

# Data aggregation:Data aggregation is used to bring data together and convey in a summary form.
"""
    It is used to group the data and we always revert back the grouped data in dictionary form.
    We use dictionary because key is immutable and key-value pair is easy to know the occurances of object.
    key-value pair
    111111111111111122222222222222222233333333333344444444444444444444445555555555555555555555555555
    1 - occurance
    2 - occurance
    3 - occurance
    It can also be used for strings.
    In case of integers, we will have to convert integer to strings because integer data types are
    non-iterable in nature.

"""

print("===========================================================")

# Aggregation of numbers:
num = 1111111111111111222222222222223333333333333333333333333344444455555555555555555555555666666666666666666666666
counter = dict()
sum_num = 0

for i in str(num):
    if i in counter:
        counter[i] += 1             # for second and further occurances
        sum_num = sum_num + int(i)
    else:
        counter[i] = 1              # for first occurances
        sum_num = sum_num + int(i)

print(counter)
print("Sum of numbers = ",sum_num)

print(" ")

# Aggregation of string:
line = "Batty botter bought soome butter but she said the butter's bitter. So she bought some better butter."
counter = dict()

for i in line:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
print(counter)                  ## It will print the coccurance of each and every character and also of space.

print(" ")

# To print occurances of words, we will have to split the string into list of words and then apply same logic to get occurances of words.

line = "Batty botter bought some butter but she said the butter bitter. So she bought some better butter"
counter = dict()
words = line.split()

for i in words:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
print(counter)

print(" ")

#List aggregation:
items = [11, 3, 5, 647, 876, "morning", "evening"]
counter = dict()

for i in items:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
print(counter)