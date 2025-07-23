
# This function performs basic arithmetic operations on two numbers.
# Parameters:
# num1 (int, float): The first number.
# num2 (int, float): The second number.
# operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').



def perform_operation(num1, num2, operation):
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
   
 
 

   
