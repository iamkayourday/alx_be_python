# Simple Calculator with Match Case
# This program performs basic arithmetic operations using match-case statements.

print(f"Welcome to the simple calculator!!!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operations = input("Choose the operation (+, -, *, /): ")

match operations:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print(f"Cannot divide by zero")
    case _:
        print(f"Invalid operation selected. Please choose from +, -, *, /")