# Printing a string using short keys of regular expressions:
import re
string = "This is my new string"

match = re.search("\w+", string)
if match:
    print(match.group())

print("="*5)

# Printing entire string using short keys:
match = re.search("\w+ \w+ \w+ \w+ \w+", string)
if match:
    print(match.group())

print("="*22)

# Working on indexing:
match = re.search("(\w+) (\w+) (\w+) (\w+) (\w+)", string)
if match:
    print(match.group(1))
    print(match.group(3))
    print(match.group(4))

print("="*38)

# Groups function: It returns the tuple.
match = re.search("(\w+) (\w+) (\w+) (\w+) (\w+)", string)
if match:
    print(match.groups())

IP validation:
import re

dir_path = r"E:\Industrial training\venv"
file_name = "ip.txt"

with open(dir_path+"/"+file_name) as input_file:
    for line in input_file:
        # print(line)
        all_ips = re.finditer("(\d+)\.(\d+)\.(\d+)\.(\d+)", line)
        # print(all_ips)
        for ip in all_ips:
            # print(ip)
            # print(ip.group())
            valid = False
            ip_address = ip.group()
            # print(ip.groups())
            for element in ip.groups():
                # print(element)
                if int(element) >= 0 and int(element) <= 255:
                    valid = True
                else:
                    valid = False
                    break
            if valid:
                print(ip_address)

# email validation:

import re

email = input("Enter your email address:")
if re.match("[a-zA-z0-9_.] + \@ + \w+ \. \w+ (\.?) (\w+)?", email, re.X):
    print("Email ID accepted!")
else:
    print("Enter a valid email ID")