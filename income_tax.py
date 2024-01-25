# Calculate income tax for the given income by adhering to the rules below
# For example, suppose the taxable income is 45000, and the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000.

# Pseudo code

# ask user's input for income
income = int(input("What is your income?: "))
print(income)
# variable for tax income holding only 0
tax_income = 0
# use if statement to calculate the given tax using the given conditions
if income <= 20000:
    below_20k = (income - 10000) *.1
    print(below_20k)
elif income >= 20000:
    below_20k = (income - 10000) *.1
    above_20k = (income - 30000) *.2
    sum = below_20k + above_20k
    print(sum)
    