def check_even(func):
    def wrapper(digit):
        return func(digit)
    return wrapper
@check_even
def is_even(digit):
    """ Checking whether a number is even """
    return digit % 2 == 0
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')