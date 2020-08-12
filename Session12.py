#Looping statements:
"""
    loops:
        for loop    : iteration
        while loop  : condition

    statement-> to run multiple times-> condition or iteration
    iterable_object-> string, list, tuple, dict, set, range, user created

    Syntax:
        for identifier in iterable_object:
            statement1
            statement2
            statement3
        else:
            statement4

        else will only get executed when for loop is executed successfully executed.
        else block is optional.

"""

#for loop with list:
cars = ["Swift","Alto","VOLVO","Jaguar"]
for i in cars:
    print(i)
    print(type(i))
print(type(cars))

print(" ")

num_str1 = [1,2,"Pen","Pencil",55,(83,98)]
for j in num_str1:
    print(j)
    print(type(j))

"""
    List functions cannot be used here as each time i is storing a different type of
    object.For a particular object which belongs to that very type, function used will show 
    result (desired one) , but for rest of the objects , it will revert back with an error.
    
"""

print(" ")

fruits = ["mango","apple","pear","lichi","orange"]
for m in fruits:
    print(m.upper())
    print(m.capitalize())
    print(m.isprintable())
    print(type(m))
print(type(fruits))
fruits.append("melon")
print(fruits)

print(" ")

#for loop with tuple:
dishes = ("paneer tikka", "butter naan", "pasta", "dosa")
for n in dishes:
    print(n)

print("----------------------------------")

#for loop with sets:
num1 = {1,"Pune",3,"India",5}
for y in num1:
    print(y)

print("----------------------------------")

#for loop with dict:
var = {1:"one", 2:"two", 3:"three", 4:"four"}
for q in var:
    print(q)                  #This statement will return back with the keys.
print(" ")
for r in var:
    print(var[r])             #This statement will return back with values.
print(" ")
for t in var:
    print(f'{t} : {var[t]}')  #This statement will return back with both keys and values.

print("----------------------------------")

#Range object: Also it can be termed as range function.
"""
    range(start,end,step)
    start -> starting number integer - optional - default value = 0
    end   -> ending value (must be one greater than the required value, like we did in slicing.)
    step  -> jump value - optional - default value = 1
    
"""
for i in range(1,11,1):
    print(i)

print(" ")

for i in range(11):
    print(i,end="\t")

for m in range(2,2):
    print(m)                #Empty object will not display any output.

print(" ")

for n in range(1,11):
    if n%2:
        print("{} is odd.".format(n))
    else:
        print("{} is even.".format(n))

print("-------------------------------------------")

#Nested for loop:
shakes = ["Mango","Berries","Banana","Chocolate","Milkshake"]
for p in shakes:
    print(p)
    for r in range(5):
        print(r)

print("---------------------------------------------------")

#Pass: It is a null operation, when executed, nothing happens.
k = int(input("Enter any number:"))
if k%2:
    print("{} is even.".format(k))
    pass                                  #Due to pass statement here, python is not throwing an error else it would have done that.

print("---------------------------------------------------")

#Break keyword: It is used to break the currently running loop, but doesn't exit the program.
#It is only applicabe for looping statements.
for m in range(1,1000000000000000):
    print(m)
    if m>=100:
        break

#for-else loop with break:
for m in range(1,1000000000000000):
    print(m)
    if m>=100:
        break

else:
    print("All good to go till now:)")

print(" ")

for m in range(1,5):
    print(m)

else:
    print("All good to go till now:)")