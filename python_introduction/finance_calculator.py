# Personal Finance Calculator
# This script calculates the total amount of money saved over a period of time.

income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

savings = income - expenses
print(f"Your monthly savings are: ${savings}")

# Projected annual savings
annual_savings = savings * 12
projected_savings = annual_savings + (annual_savings * 0.05) # Assuming a 5% interest rate
print(f"Projected savings after one year, with interest, is: ${projected_savings}")

# Output: if the user inputs 5000 for income and 4000 for expenses, the output will be:
        # Your monthly savings are: $1000
        # Projected savings after one year, with interest, is: $12600