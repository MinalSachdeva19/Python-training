l = [1,1,2,3,4,4,4,5,5,5,6]
distinct = dict()
for i in l:
    if i in distinct:
        distinct[i] += 1
    else:
        distinct[i] = 1
print("Distinct ->",list(distinct.keys()))
print("Unique->",list(filter(lambda x:distinct[x]==1,distinct)))
print("Duplicate->",list(filter(lambda x:distinct[x]!=1,distinct)))