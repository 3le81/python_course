"""
1. Create an if-elif-else statement, with a variety of responses determined
by the age the user is going to enter when requested.
2. Make sure that the if-elif-else statements work properly
in terms of the logical tests applied to the ages.
"""
# Create an integer variable called age with the input for the user to put the age:
age = int(input("How old are you?"))

# If-elif-else statements created with responses depending on the user's age, in logical order:
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hil!!")
elif age < 13:
    print("You qualify for the kiddie discount")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number")
