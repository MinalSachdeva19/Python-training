# Built-in functions in strings:
print(dir(str))
"""
    'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
    'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
    'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
    'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 
    'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
    'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
"""

string = "this is my first string."
print(string.capitalize())
print("========================================================")
print(string.casefold())
# Return a version of the string suitable for caseless comparisons.
print("========================================================")
print(string.center(45, "&"))
# Return a centered string of length width.
print("========================================================")
print(string.count("s"))
# Return the number of non-overlapping occurrences of substring sub in string S[start:end].
print("========================================================")
print(string.encode(encoding="UTF-16"))
print("========================================================")
print(string.endswith("g"))
print("========================================================")
str1 = "Hello/tThere"
print(str1.expandtabs())
# Return a copy where all tab characters are expanded using spaces.
print("========================================================")
print(string.find("s"))
print("========================================================")
print('Oh wow! {}'.format(string))
# Return a formatted version of String.
print("========================================================")
# print()
print("========================================================")
print(string.index("m"))
# Return the lowest index in S where substring sub is found.
print("========================================================")
string1 = "HelloWorld"
print(string.isalpha())
print(string1.isalpha())
# Return True if the string is an alphabetic string, False otherwise.
print("========================================================")
print(string.isalnum())
# Return True if the string is an alpha-numeric string, False otherwise.
print("========================================================")
print(string.isascii())
# Return True if all characters in the string are ASCII, False otherwise.
print("========================================================")
print(string.isdecimal())
# Return True if the string is a decimal string, False otherwise.
print("========================================================")
print(string.isdigit())
# Return True if the string is a digit string, False otherwise.
print("========================================================")
str2 = "9876"
print(str2.isdigit())
print("========================================================")
print(string.isidentifier())
print("========================================================")
print(string.islower())
print("========================================================")
print(string.isnumeric())
print(str2.isnumeric())
# Return True if the string is a numeric string, False otherwise.
print("========================================================")
print(string.isprintable())
# Return True if the string is printable, False otherwise.
print("========================================================")
print(string.isspace())
# Return True if the string is a whitespace string, False otherwise.
print("========================================================")
print(string.istitle())
# Return True if the string is a title-cased string, False otherwise.
print("========================================================")
print(string.isupper())
print("========================================================")
print("@".join(["This", "is", "my", "first", "Assignment"]))
# Concatenate any number of strings.
# The string whose method is called is inserted in between each given string. The result is returned as a new string.
print("========================================================")
print(string.ljust(100,"&"))
# #Return a left-justified string of length width.
print("========================================================")
string2 = "THIS IS MY ASSIGNMENT!"
print(string2.lower())
print("========================================================")
string3 ="      This is my string !!!!     "
print(string3.lstrip())
#Return a copy of the string with leading whitespace removed.
print("========================================================")
fruit = "My favourite fruit is Kiwi!"
intab = "aeiou"
outtab = "12345"
statement = fruit.maketrans(intab,outtab)
print(statement)
print(fruit.translate(statement))
print("========================================================")
print(string.partition("is"))
#Partition the string into three parts using the given separator. Return the result in the form of tuple.
print("========================================================")
print(fruit.replace("Kiwi","Guava"))
#Return a copy with all occurrences of substring old replaced by new.
print("========================================================")
string4 = "let it be, let it be, let it be"
print(string4.rfind("let it"))
print(string4.rfind("is"))
print(string4.rfind("be"))
#Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].
print("========================================================")
print(string4.rindex("let it be"))
#print(string4.rindex("to"))            OP:-ValueError: substring not found
#Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].
print("========================================================")
print(string.rjust(34,"%"))
#Return a right-justified string of length width.
print("========================================================")
print(string4.rpartition("it"))
#Partition the string into three parts using the given separator (begin from right).
print("========================================================")
mail = "From: yours@gmail.com"
print(string.rsplit( ))
print(mail.rsplit("@"))
#Return a list of the words in the string, using sep as the delimiter string.
print("========================================================")
print(string3.rstrip())
#Return a copy of the string with trailing whitespace removed.
print("========================================================")
print(string4.split())
#Return a list of the words in the string, using sep as the delimiter string.
print("========================================================")
cars = 'There are \n so many cars\n But my favourite \n is Audi'
print(cars.splitlines())
print("========================================================")
print(mail.startswith("From:"))
#Return True if S starts with the specified prefix, False otherwise.
print("========================================================")
print(string3.strip())
#Return a copy of the string with leading and trailing whitespace removed.
print("========================================================")
print(string4.swapcase())
#Convert uppercase characters to lowercase and lowercase characters to uppercase.
print("========================================================")
print(string3.title())
#Return a version of the string where each word is titlecased.
#More specifically, words start with uppercased characters and all remaining cased characters have lower case.
print("========================================================")
print(string.upper())
print("========================================================")
print(string.zfill(30))
#Pad a numeric string with zeros on the left, to fill a field of the given width.
#The string is never truncated.
print("*********************************************************************************************************************")


# Built-in functions in lists:
print(dir(list))
"""
     'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""
list1 = [893, 748, 84, 847, "Mumbai", 84, "Delhi", "Python", 6459, 480, "ML", 84]
#         0    1   2    3      4      5     6         7        8    9    10   11
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])
print(list1[6])
print(list1[7])
print(list1[8])
print(list1[9])
print(list1[10])
print(list1[11])
print("========================================================")
list1.append('Training')
print(list1)
print("========================================================")
list2 = list1.copy()
print(list2)
print("========================================================")
print(list1.count(84))
print("========================================================")
list3 = [757, "a", 9488, "b", 394]
list1.extend(list3)
print(list1)
#Extend list by appending elements from the iterable.
print("========================================================")
print(list1.index(84))
print(list1.index("b"))
#After appending Training , its index will come 16.
print("========================================================")
list1.insert(3,"Minal")
print(list1)
print("========================================================")
print(list1.pop(4))
#Remove and return item at index (default last).
print("========================================================")
list1.remove(84)
print(list1)
#Remove first occurrence of value.
print("========================================================")
list3.reverse()
print(list3)
#Reverse IN PLACE.
print("========================================================")
list4 = ["apple","mango","Chocolates","banana","Pear"]
list4.sort()
print(list4)
print("========================================================")
print(list3.clear())
print("========================================================")
print(list3)

#End !