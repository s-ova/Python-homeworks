lst = [0, 1, 0, 12, 3, 9, 0, 0, 7, -2, 24]
index = 0
for i in range(len(lst)):
    if lst[i] != 0:
        lst[index] = lst[i]
        index += 1
for i in range(index, len(lst)):
    lst[i] = 0
print(lst)