'''
Program: investment.py
Author: Kainan Smith
Class: CIS Seniors
Date: 9/22/25

1. The inputs are:
    Starting investment amount
    Number of years
    Interest rate (an Int percent)

2. The report is displayed in tabular form with a header
3. Computations and outputs:
    for each year of the investment
        compute the interest and add it to the investment
        print a formatted row of results for that year
4. The ending investment and interest you have paid in total are also displayed
'''
print("\n\nMy Investment Calculator")
print("=" * 25)
# Accept the inputs
startingAmount = float(input("Enter the starting investment amount: "))
numYears = float(input("Enter the number of years to invest: "))
interestRate = float(input("Enter the interest percentage: "))

# Convert the interest rate to a decimal number
interestRate = 1 + (interestRate / 100)
endInvest = startingAmount * (interestRate ** numYears)
print("Your total invested amount is ", round(endInvest, 2))

# Initialize the accumulator for the interest


# Display the header for the table


# Compute and display the results for each year


# Display the totals for the period