import random
lst = [random.randint(1,100) for _ in range(random.randint(3, 10))]
new_list = [lst[0], lst[2], lst[-2]]
print("Original list:", lst)
print("New list:", new_list)
