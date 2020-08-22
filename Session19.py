# Lambda and list Comprehension together: To find prime number between 2-100
print(list(filter(lambda x:True if all([x%i for i in range(2,x)]) else False, range(2,101))))

print("="*100)

# Encoding: String functions:
string = "This is my String"
encoded_string = string.encode(encoding="UTF-16")
print(encoded_string)

# Decoding:
print(encoded_string.decode(encoding="UTF-16"))

print("="*100)

# File handling:
"""
    Two parts:
        1. open():  To create, read, write and delete data into or from a file in our operating systemm
        2. close(): To close the file which was opened once, if not closed, file can get corrupted. 
    There are tow ways to open a file:
        1. When Python take care of closing the file once opened.
            Syntax: with open(path) as identifier: 
        2. When user take care of closing the file once opened. 
"""
# 1. When Python take care of closing the file once opened.
dir_name = r"E:\Industrial training"
file_name = "File handling file.txt"
actual_path = dir_name+"\\"+file_name           # This will create a new file on given path.
with open(actual_path, mode = "w") as Minal:    # Writing something in file. Minal here is just an identifier, it could be anything.
    Minal.write("Welcome to file handling file.\n")
    Minal.write("This is my lecture 19 in Python Training program.\nGood to go till now.")

# to append something in the existing file:
dir_name = r"E:\Industrial training"
file_name = "File handling file.txt"
actual_path = dir_name+"\\"+file_name
with open(actual_path, mode = "a") as Minal:     # Appending something .
    Minal.write("\nHi!\n")
    Minal.write("Hello!\n")
    Minal.write("How are you!\n")

# 2. When user take care of closing the file once opened:
dir_name = r"E:\Industrial training"
file_name = "File handling file.txt"
actual_path = dir_name+"\\"+file_name
Minal = open(actual_path,mode="a")
Minal.write("Hope you are fine?\n")
Minal.write("End of file!\n")
Minal.close()

# To create a file's backup: This will create the backup of the file
dir_name = r"E:\Industrial training"
file_name = "File handling file.txt"
actual_path = dir_name+"\\"+file_name
backup_file = "Backup.txt"
with open(dir_name+"\\"+backup_file, mode = "w") as file:
    source = open(actual_path,mode="r")
    file.writelines(source.readlines())
    source.close()