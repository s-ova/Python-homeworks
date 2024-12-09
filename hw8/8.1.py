def add_one(some_list):
    if not some_list:
        return [1]
    if some_list[-1] < 9:
        some_list[-1] += 1
        return some_list
    some_list[-1] = 0
    return add_one(some_list[:-1]) + [0]
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")