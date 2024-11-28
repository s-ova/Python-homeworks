lst = [0, 1, 7, 2, 4, 8, 10, 15, 23, -4]
if lst:
    even_sum = sum(value for index, value in enumerate(lst) if index % 2 == 0)
    result = even_sum * lst[-1]
else:
    result = 0
print(result)