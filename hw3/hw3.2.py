lst = [8,36,7,-1,'bo']
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)