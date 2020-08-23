name = input("Enter a name:")
name = name.split()                 # Will convert string to list.
print(name)
if len(name) == 1:
    print("Hello," + name[0].capitalize())
elif len(name) == 2:
    print("Hello," + name[-1].capitalize()+ " "+ name[0].capitalize())
else :
    print("Hello,"+name[0][0].capitalize()+"."+name[1][0].capitalize()+"."+name[2].capitalize())
