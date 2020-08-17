# Prime Number using List Comprehension:
for num in range (2,101):
    if all([num%i for i in range(2,num)]):
        print("{} is Prime.".format(num))
    else:
        print("{} is not Prime.".format(num))

print("======================================================================================")

m = [num for num in range (2,101) if all([num%j for j in range (2,num)])]
print(m)

print("======================================================================================")


print(all([]))              #Syntax of all function.
print(all([[]]))            #empty list in all.
print(all([2%2]))

print("======================================================================================")

# List to dict:
fruits = ["apple", "mango", "pear", "kiwi"]
print({i:fruits[i] for i in range(len(fruits))})

print("======================================================================================")

# List to dict using enumerate :
"""
    enumerate function returns the result in tuple form and that result is necessarily within the length of the iterable
    object. Earlier we passed length of object in the range function, but in enumerate , we simply need to pass the object.
"""
fruits = ["apple", "mango", "pear", "kiwi"]
print({i:j for i,j in enumerate(fruits)})

print({i:j for i,j in enumerate(fruits,start=34)})

print("======================================================================================")

# Enumerate with strings:
var = "Minal"
var_enum = enumerate(var,start=13)
for i in var_enum:
    print(i)

# We can convert list to tuple using enumerate, and can also convert list to tuple than to dictionary:
# list -> tuple(enumerate) -> dictionary
# If we have two lists also , then even it is possible to use enumerate.

print("======================================================================================")

students = ["Rahul", "Rita", "Rupam", "Renu"]
class_id =[3,14,79,37]
print(enumerate(students))
print(list(enumerate(students)))
print(dict(list(enumerate(students))))

print("======================================================================================")

# When we have two lists and we want to use one as key and other as value in dictionary:
students = ["Ram", "Sham", "Geeta", "Seeta"]
class_id =[23,54,78,34]
print({class_id[i]:students[i] for i in range(len(students))})      #i is needed to travel from index of students.

print("======================================================================================")

# Printing the above two lists as dictionary without loop and list comprehensions:
# Zip function:
students = ["Ram", "Sham", "Geeta", "Seeta"]
class_id =[23,54,78,34]
print(zip(students,class_id))
# List of tuple:
print(list(zip(students,class_id)))
# List of tuple to dict:
print(dict(list(zip(students,class_id))))

print("======================================================================================")

#Zip function to print as tuple:
for i in zip(students,class_id):
    print(i)

print("======================================================================================")

# applepie -> to find indexes in aggregated list format:
"""
    expected output:
        a - [0]
        p - [1,2,5]
        l - [3]
        e - [4,7]
        i - [6]

"""

input = "applepie"
counter = dict()
idx = 0
for i in input:
    if i in counter:
        counter[i].append(input.index(i, idx, len(input)))
    else:
        counter[i] = [input.index(i,idx, len(input))]
    idx += 1

for i in counter:
    print("{} - {}".format(i,counter[i]))


