number = int(float(input("enter a 4-digit number: ")))
digit1 = number // 1000  # First number
digit2 = (number % 1000) // 100  # Second number
digit3 = (number % 100) // 10  # Third number
digit4 = number % 10  # Fourth number
print(digit1)
print(digit2)
print(digit3)
print(digit4)