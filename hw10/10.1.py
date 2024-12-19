def pow(x):
    return x ** 2
def some_gen(begin, end, func):
    if end <= 0:
        return
    yield begin
    yield from some_gen(func(begin), end - 1, func)
gen = some_gen(2, 4, pow)
from inspect import isgenerator
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')