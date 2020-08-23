l = [3,7,6,2]
count = 0
total = 3+7+6+2
for i in l:
    if (total-i)%i == 0:
        count += 1
    else:
        continue
print(count)