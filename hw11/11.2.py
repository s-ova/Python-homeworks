def generate_cube_numbers(end):
    return (num ** 3 for num in range(2, int(end ** (1 / 3)) + 2) if num ** 3 <= end)
from inspect import isgenerator
gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'since it is less than 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 in a cube is 125, and it is already more than 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 in a cube is 1000'
print('OK')