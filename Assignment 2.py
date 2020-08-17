# applepie -> to find indexes in aggregated list format:
"""
    expected output:
        a - [0]
        p - [1,2,5]
        l - [3]
        e - [4,7]
        i - [6]

"""

input = "applepie"
counter = dict()
idx = 0
for i in input:
    if i in counter:
        counter[i].append(input.index(i, idx, len(input)))
    else:
        counter[i] = [input.index(i,idx, len(input))]
    idx += 1

for i in counter:
    print("{} - {}".format(i,counter[i]))