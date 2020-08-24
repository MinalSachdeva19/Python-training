import os
# To find the current working directory:
print(os.getcwd())

# To change the current working directory:
print(os.chdir(r"C:\Users\minal\Documents"))            # Will always return none
print(os.getcwd())

# To get all the directories present at some path:
os.chdir(r"E:\Industrial training\venv")
print(os.listdir())

# To check if the given location is a directory:
print(os.path.isdir(r"E:\Industrial training\venv"))
print(os.path.isdir(r'E:\Industrial training\venv\Sample.txt'))

# To check if the given location is a file:
print(os.path.isfile(r"E:\Industrial training\venv"))
print(os.path.isfile(r'E:\Industrial training\venv\Sample.txt'))

# Write a program to remove a file.
import os
user_dir = input("Enter your directory:")
if os.path.isdir(user_dir):
    os.chdir(user_dir)
    print(os.listdir())
    file_name = input("Enter a file name:")
    if os.path.isfile(file_name):
        os.remove(file_name)                    # Will delete the file from that directory.
else:
    print("Enter a valid directory.")

# Program to traverse recursively inside folders and subfolders:
import os
directory = r"E:\Industrial training\venv"
for dirpath,dirname,filenames in os.walk(directory):
    # print(dirpath)
    # print(dirname)
    # print(filenames)
    for file in filenames:
        if file.endswith(".py"):
            print(file)
            print(os.path.join(dirpath,file))
