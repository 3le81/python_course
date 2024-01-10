"""
1. Ask to enter the name and save it into a variable
2. Ask to enter the age and save it into a variable
3. Ask to enter the house number and save it into a variable
4. Ask to enter the street name and save it into a variable
5. Print the string using the f"", including all the variables collected in the previous steps.
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")
print(
    f"This is {name}, is {age} years old and lives at {house_number} on {street_name}.")
