import string
import keyword
while True:
    name = input("Enter a string to check if it can be a variable name (or 'exit' to quit): ")
    if name.lower() == "exit":
        print("Good Luck!")
        break
    if name in keyword.kwlist:
        print(False)
        continue
    if name[0].isdigit():
        print(False)
        continue
    if any(char.isupper() for char in name):
        print(False)
        continue
    if any(char in string.punctuation.replace("_", "") for char in name):
        print(False)
        continue
    if name.count("__") > 0 or name.count("__") > 1  :
        print(False)
        continue
    print(True)