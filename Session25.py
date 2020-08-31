# Regular Expressions:
import re

# match() function:Try to apply the pattern at the start of the string,
# returning a Match object, or None if no match was found.
string = "This is my string which have some numbers like 83"
Match = re.match("This", string, flags= re.I)

print(Match)
print(type(Match))
print("-"*45)
if Match:
    print(Match.start())
    print(Match.end())
    print(Match.span())
    print(Match.group())
else:
    print("Pattern not found.")

print("="*8)

# search() function:Scan through string looking for a match to the pattern,
# returning a Match object, or None if no match was found.
string = "This is my string which have some numbers like 83"
Match = re.search("some", string, flags= re.I)

if Match:
    print(Match.start())
    print(Match.end())
    print(Match.span())
    print(Match.group())
else:
    print("Pattern not found.")

print("-"*8)
Match = re.search("83", string, flags= re.I)

if Match:
    print(Match.start())
    print(Match.end())
    print(Match.span())
    print(Match.group())
else:
    print("Pattern not found.")

print("="*8)

# period operator: Creates an empty container.
Match = re.search("8.", string, flags= re.I)

if Match:
    print(Match.start())
    print(Match.end())
    print(Match.span())
    print(Match.group())
else:
    print("Pattern not found.")

print("-"*8)
Match = re.search("r...........", string, flags= re.I)

if Match:
    print(Match.start())
    print(Match.end())
    print(Match.span())
    print(Match.group())
else:
    print("Pattern not found.")


print("-"*15)
Match = re.search("...................", string, flags= re.I)

if Match:
    print(Match.start())
    print(Match.end())
    print(Match.span())
    print(Match.group())
else:
    print("Pattern not found.")

print("-"*20)
Match = re.search(".....8", string, flags= re.I)

if Match:
    print(Match.start())
    print(Match.end())
    print(Match.span())
    print(Match.group())
else:
    print("Pattern not found.")

print("="*10)
# Charclass and occurrence operator:
string = "This is my string which have some numbers like 83 and IP address is 225.225.225.225"
Match = re.search("[0-9]{1,}.[0-9]{1,}.[0-9]{1,}.[0-9]{1,}", string, flags= re.I)

if Match:
    print(Match.start())
    print(Match.end())
    print(Match.span())
    print(Match.group())
else:
    print("Pattern not found.")

print("-"*15)
# To suppress the power of "." -> period operator, use back slash "\"
string = "This is my string which have some numbers like 83 and IP address is 225.225.225.225"
Match = re.search("[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}", string, flags= re.I)

if Match:
    print(Match.start())
    print(Match.end())
    print(Match.span())
    print(Match.group())
else:
    print("Pattern not found.")

print("="*15)

string = "This is mmmmmmmmmmmmmmmmmmmmmmmmyyyyyyyyyy string which have some numbers like 83"
# Match = re.search("my{0,5}", string, flags= re.I)
Match = re.search("my{1,5}", string, flags= re.I)

if Match:
    print(Match.start())
    print(Match.end())
    print(Match.span())
    print(Match.group())
else:
    print("Pattern not found.")

# Password Validation and acceptance:
import re

count = 0
while count < 3:
    password = input("Enter your password (Must have at least one char(one upper and one lower each), one special char, one digit, length > 8) : ")
    if re.search("[a-zA-Z]", password):
        if re.search("[0-9]", password):
            if re.search("[$@#%^&*!]", password):
                if len(password) >= 8:
                    print("Password accepted!")
                    break
                else:
                    print("Length of password should be equal to or greater than 8.")
            else:
                print("Password should contain at least one special character - $@#%^&*! .")
        else:
            print("Password should contain at least one digit.")
    else:
        print("Password should contain at least one character.")
    count += 1