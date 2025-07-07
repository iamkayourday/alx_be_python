# User Input Age Calculator
# This script calculates the user's age.

age = int(input("How old are you? "))
current_year = 2023
future_year = 2050

future_age = future_year - current_year + age
print(f"In {future_year}, you will be {future_age} years old.")

# Output: If the user is 30 years old, the output will be:
# In 2050, you will be 57 years old.