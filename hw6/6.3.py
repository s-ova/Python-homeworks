number = int(input("Enter an integer: "))
while number > 9:
    output = 1
    for digit in str(number):
        output *= int(digit)
    number = output
print("Result:", number)