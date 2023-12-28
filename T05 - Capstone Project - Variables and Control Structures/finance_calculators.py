import math

# Initial message for the user with the instructions to follow
print("Choose an option:")
print("- 'investment' to calculate the amount of interest you'll earn on your investment")
print("- 'bond' to calculate the amount you'll have to pay on a home loan")

# Get user input for the choice
calculation_type = input("Enter either 'investment' or 'bond' to proceed: ").lower()

# Check user's choice
if calculation_type == 'investment':
    # Get input for investment calculation
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100
    t = int(input("Enter the number of years you plan on investing: "))
    interest = input("Enter 'simple' or 'compound' interest: ").lower()

    # Perform investment calculation based on user input
    if interest == 'simple':
        A = P * (1 + r * t)
    elif interest == 'compound':
        A = P * math.pow((1 + r), t)
    else:
        # Display an error message for invalid interest input
        print("Invalid input. Please enter 'simple' or 'compound'.")
        exit()

    # Display the result of the investment calculation (R currency used as shown in the Capstone Project examples)
    print(f"The total amount after {t} years will be: R{A:.2f}")

elif calculation_type == 'bond':
    # Get input for bond calculation
    P = float(input("Enter the present value of the house: "))
    i = (float(input("Enter the annual interest rate: ")) / 100) / 12
    n = int(input("Enter the number of months for bond repayment: "))

    # Perform bond calculation based on user input
    repayment = (i * P) / (1 - (1 + i)**(-n))

    # Display the result of the bond calculation
    print(f"The monthly bond repayment will be: R{repayment:.2f}")

else:
    # Display an error message for invalid menu choice
    print("Invalid input. Please enter 'investment' or 'bond'.")
