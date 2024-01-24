# A revised version of the Capstone Project T05, Finance Calculator, accepting a feedback about not to use single characters as variables, but more meaningful names instead

import math

# Initial message for the user with the instructions to follow
print("Choose an option:")
print("- 'investment' to calculate the amount of interest you'll earn on your investment")
print("- 'bond' to calculate the amount you'll have to pay on a home loan")

# Get user input for the choice
calculation_type = input(
    "Enter either 'investment' or 'bond' to proceed: ").lower()

# Check user's choice
if calculation_type == 'investment':
    # Get input for investment calculation
    principal = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(
        input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    # Perform investment calculation based on user input
    if interest_type == 'simple':
        future_value = principal * (1 + interest_rate * years)
    elif interest_type == 'compound':
        future_value = principal * math.pow((1 + interest_rate), years)
    else:
        # Display an error message for invalid interest input
        print("Invalid input. Please enter 'simple' or 'compound'.")
        exit()

    # Display the result of the investment calculation (R currency used as shown in the Capstone Project examples)
    print(f"The total amount after {years} years will be: R{future_value:.2f}")

elif calculation_type == 'bond':
    # Get input for bond calculation
    present_value = float(input("Enter the present value of the house: "))
    annual_interest_rate = (
        float(input("Enter the annual interest rate: ")) / 100) / 12
    repayment_months = int(
        input("Enter the number of months for bond repayment: "))

    # Perform bond calculation based on user input
    monthly_repayment = (annual_interest_rate * present_value) / \
        (1 - (1 + annual_interest_rate)**(-repayment_months))

    # Display the result of the bond calculation
    print(f"The monthly bond repayment will be: R{monthly_repayment:.2f}")

else:
    # Display an error message for invalid menu choice
    print("Invalid input. Please enter 'investment' or 'bond'.")
