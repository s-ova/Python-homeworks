number = int(input("enter a 5-digit number: "))
reversed_number = (
        (number % 10) * 10000 +  # The last number becomes the first
        ((number // 10) % 10) * 1000 +  # The penultimate digit becomes the second
        ((number // 100) % 10) * 100 +  # The middle number becomes the third
        ((number // 1000) % 10) * 10 +  # The second digit becomes the fourth
        (number // 10000)  # The first digit becomes the last
)
print("Reverse the number:", reversed_number)