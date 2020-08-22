# Lambda Function: It is an anonymous function which is user defined function,
# contains "n" number of arguments and returns a singular value.
"""
    SYNTAX: lambda argument: expression
            def function(args):
"""
# Square of numbers:
print(list(map(lambda x: x**2,range(1,11))))

print("="*50)

# num = input("Enter a number:")
# print(list(map(lambda x: x**2,num[1:])))        # WIll return empty list.

print("="*50)

print(list(map(lambda x: x**2,range(9))))

print("="*50)

# Cube of numbers:
print(list(map(lambda x: x**3,range(1,11))))

# Without passing argument in lambda:
print_hi = lambda : print("Hello Minal")
print_hi()

# print_hi = lambda x:"minal"
# print_hi(x)                         # Nothing will get displayed as we are not printing anything.

print("="*100)

# Iterating lambda as a function:
print((lambda x:x**3)(9))
print((lambda x,y,z:x*y*z)(9,2,2))   # passing multiple arguments.

print("="*100)

# We use lambda function to check if any condition is True or False:
print(list(filter(lambda x:x%2==0,range(2,30))))    # Even numbers
print(list(filter(lambda x:x%20,range(2,30))))      # Odd numbers
print(list(filter(lambda x:x>=10,range(2,30))))     # Some condition

print("="*100)

# One of the use case of lambda is Sorting.
"""
    There is already a built in function associated with list i.e. sort. But for rest of the Data Structures of Python,
    there is no built-in function named sort.
    1. Sorting of list      
    2. Sorting of Tuple
    3. Sorting of Sets
    4. Sorting of Dictionary  
"""
# Sorting a list:
languages = ["C", "R", "Ruby", "Dart", "Python", "Java"]
languages.sort()
print(languages)

print("="*78)

# Sorting a tuple: There is no built in function to sort a tuple. So we will sort a list of tuples so
# as to get the desired output.
languages = [(11,"C"), (25,"R"), (8,"Ruby"), (13,"Dart"), (5,"Python"), (9,"Java")]
languages.sort()            # It is sorting on the basis of zeroth indexes of each of the tuple.
print(languages)

print("-"*105)

languages.sort(key=lambda x:x[1])   # To sort on the basis of first indexes of list of tuples.
print("Programming Languages are:", languages)

languages.sort(key=lambda x:x[1], reverse=True)   # To sort on the basis of first indexes of list of tuples.
print("Programming Languages are:", languages)    # In descending order.

print("="*105)

# Sorted function: It can take any type of iterable object. It always returns a list.
"""
sorted(iterable, /, *, key=None, reverse=False)    
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
"""

# Sorting of tuple:
languages = ("C", "R", "Ruby", "Dart", "Python", "Java")
sorted_languages = sorted(languages)                    # will return a sorted list.
print(sorted_languages)

languages = ("C", "R", "Ruby", "Dart", "Python", "Java")
sorted_languages = tuple(sorted(languages))             # will return a sorted tuple.
print(sorted_languages)

print("-"*45)

# Sorting of Sets:
languages = {"C", "R", "Ruby", "Dart", "Python", "Java"}
sorted_languages = sorted(languages)                    # will return a sorted list.
print(sorted_languages)

languages = {"C", "R", "Ruby", "Dart", "Python", "Java"}
sorted_languages = set(sorted(languages))               # will return an unordered set as set returns an unordered result.
print(sorted_languages)


print("-"*45)

# Sorting of Dictionaries: value based sorting.
languages = {11:"C", 25:"R", 8:"Ruby", 13:"Dart", 5:"Python", 9:"Java"}
sorted_languages = sorted(languages)                    # will return a sorted list of keys only.
print(sorted_languages)

sorted_keys = sorted(languages,key= lambda x:languages[x])
print(sorted_keys)                                      # Sorted keys on the basis of values.

for i in sorted_keys:
    print("{} - {}".format(i,languages[i]))             # This will only print the result but not in dictionary.

d = dict()
for i in sorted_keys:
    d[i] = languages[i]
print("Sorted dictionary is: ", d)

