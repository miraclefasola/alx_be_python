monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"monthly saving is: {monthly_savings}")
print(f"projected annual savings is: {projected_savings}")