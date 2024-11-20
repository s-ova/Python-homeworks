number_a = float(input("Enter the first number: "))
operation = input("Enter an operation (+, -, *, /): ")
number_b = float(input("Enter the second number: "))
if operation == "+":
    result = number_a + number_b
    print("Result:", result)
elif operation == "-":
    result = number_a - number_b
    print("Result:", result)
elif operation == "*":
    result = number_a * number_b
    print("Result:", result)
elif operation == "/":
  if number_b == 0:
    print("Error: Division by zero is not allowed!")
  else:
    result = number_a / number_b
    print("Result:", result)
else:
  print("Error: Invalid operation!")