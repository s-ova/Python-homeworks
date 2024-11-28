lst = [0, 1, 0, 12, 3, 8, 9, -1, 0, 5, 9, 2]
result = []
for i in range(len(lst)):
    if lst[i] != 0:
        result.append(lst[i])
result.extend([0] * (len(lst) - len(result)))
print(result)