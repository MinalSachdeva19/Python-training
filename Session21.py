# To know that when a file was created or modified:
import os
var = r"E:\Industrial training\venv"
mtime = os.path.getmtime(var)
print(mtime)                        # This will return the epoch time when it was modified last.
print(type(mtime))

print("===============================")

# Write a program to find number of ratings for each movie and list down in decreasing order.
dir_path = r"E:\Industrial training\Python lectures"
file_name = "ratings.dat"
movie_count = dict()
with open(os.path.join(dir_path,file_name)) as ratings:
    for line in ratings:
        line = line.strip()
        elements = line.split("::")
        movie_id = int(elements[1])
        if movie_id in movie_count:
            movie_count[movie_id] += 1
        else:
            movie_count[movie_id] =1
for movieid, moviecount in sorted(movie_count.items(), key = lambda x:x[1], reverse=True):
    print(f"MOVIE ID: {movieid} has count: {moviecount}")

print("==========================================================================================")

# If the constraint is for ratings =5:
dir_path = r"E:\Industrial training\Python lectures"
file_name = "ratings.dat"
movie_count = dict()
with open(os.path.join(dir_path,file_name)) as ratings:
    for line in ratings:
        line = line.strip()
        elements = line.split("::")
        movie_id = int(elements[1])
        if elements[2] == "5":
            if movie_id in movie_count:
                movie_count[movie_id] += 1
            else:
                movie_count[movie_id] =1
for movieid, moviecount in sorted(movie_count.items(), key = lambda x:x[1], reverse=True):
    print(f"MOVIE ID: {movieid} has count: {moviecount}")

print("===============================")

# Math module:
import math
print(math.pi)
print(math.sqrt(50))
# math.asin(30)
print(math.atan(90))
print(math.factorial(7))

print("==========================")

# datetime module:A date in Python is not a data type of its own, but we can import
# a module named datetime to work with dates as date objects.
from datetime import datetime
print(datetime.now())
print(datetime.now().date())
print(datetime.now().year)

print("--------------")

# To add a day in current day:
current_date = datetime.now().date()
old_date = datetime(2018,1,4)

# print(current_date+1)           # Error:unsupported operand type(s) for +: 'datetime.date' and 'int'

# timedelta class: returns the gap/ difference between two dates.
from datetime import datetime
from datetime import timedelta

current_date = datetime.now()
old_date = datetime(2018,1,4)

oneday = timedelta(1)
twodays = timedelta(2)
print(current_date + oneday)                # + operator overloaded: earlier we used it for int and string and now for datetime module.
print(current_date + twodays)

print(current_date > old_date)
print(current_date - old_date)

