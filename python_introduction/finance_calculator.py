# Personal Finance Calculator
Monthly_income = int(input("Enter your monthly income: "))
Monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = Monthly_income - Monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your montly savings is: ", monthly_savings)
print("Your projected annual savings is: ", projected_savings)