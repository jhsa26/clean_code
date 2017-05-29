a = [2, 4, 5, 6]
b = [3, 4]

print list(set(a) - set(b))

temp = [item for item in a if item not in b]

work = range(10)
for i in temp:
    print work[i]
