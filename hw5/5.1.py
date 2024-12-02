import string
import keyword
def is_valid_variable(name):
    if name in keyword.kwlist:
        return False
    if name[0].isdigit():
        return False
    if name.count('_') > 1:
        return False
    for char in name:
        if char not in string.ascii_lowercase + string.digits + '_':
            return False
    if any(c.isupper() for c in name):
        return False
    return True
while True:
    user_input = input("Enter a string to check if it can be a variable name (or 'exit' to quit): ").strip()
    if user_input.lower() == "exit":
        print("Good Luck!")
        break
    result = is_valid_variable(user_input)
    print(result)