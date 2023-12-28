# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Syntax error: missing parentheses in the print statement
print("Welcome to the error program")

# Syntax error: incorrect indentation
print("\n")

# Logical error: using the equality operator instead of the assignment operator
# Runtime error: attempting to convert a string with non-numeric characters to an integer
# Fix: Change '==' to '=' in age_Str assignment and use split to extract numeric part
age_Str = "24 years old"
# Extracting the numeric part from the string using split and converting it to an integer
age = int(age_Str.split()[0])

# Syntax error: Missing parentheses in the print statement
print("I'm " + str(age) + " years old.")

# Runtime error: not converting years_from_now to an integer before performing addition
# Syntax error: incorrect indentation for the years_from_now section
# Fix: Convert years_from_now to an integer
years_from_now = "3"
total_years = age + int(years_from_now)

# Syntax error: Missing parentheses in the print statement
print("The total number of years: " + str(total_years))

# Logical error: Using an undefined variable name ('total') when calculating total_months
# Fix: Change 'total' to 'total_years' when calculating total_months
total_months = (total_years * 12) + 6  # Added the 6 months directly

# Syntax error: Missing parentheses in the print statement
# Using an f-string to format the output
print(f"In 3 years and 6 months, I'll be {total_months} months old")


# HINT, 330 months is the correct answer
