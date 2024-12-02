while True:
    num1 = float(input("Enter the first number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    if operation == "+":
        result = num1 + num2
        print("Result:", result)
    elif operation == "-":
        result = num1 - num2
        print("Result:", result)
    elif operation == "*":
        result = num1 * num2
        print("Result:", result)
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Invalid operation!")
    continue_calculation = input(
         "Do you want to perform another calculation? (yes/y to continue): ").lower()
    if continue_calculation not in ["yes", "y"]:
            print("Until next time!")
            break
