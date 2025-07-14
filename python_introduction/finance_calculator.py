# Personal Finance Calculator
# This script calculates the total amount of money saved over a period of time.

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

interest_rate = 0.05
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

print(f"Your monthly savings: ${monthly_savings:.2f}")
print(f"Your projected annual savings one year, with interest, is: ${projected_annual_savings:.2f}")

# Output: if the user inputs 5000 for income and 4000 for expenses, the output will be:``
        # Your monthly savings are: $1000
        # Your projected savings after one year, with interest, is: $12600