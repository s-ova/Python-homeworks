def common_elements():
    multiples_of_3 = set()
    multiples_of_5 = set()
    for x in range(100):
        if x % 3 == 0:
            multiples_of_3.add(x)
        if x % 5 == 0:
            multiples_of_5.add(x)
    return multiples_of_3 & multiples_of_5
print(common_elements())