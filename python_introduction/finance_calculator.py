income_monthly = int(input("Enter your monthly income: "))
expenses_monthly = int(input("Enter your total monthly expenses: "))
savings_monthly = income_monthly - expenses_monthly

projected_savings = savings_monthly  * 12 + (savings_monthly *12 * 0.05)

print("Your monthly savings are $",savings_monthly)
print("Projected savings after one year, with interest, is: $",projected_savings)