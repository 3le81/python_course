# Optional challenge : Magic Lands

characters = ["Alice", "Stitch", "Belle"]
user_choice = input("Choose a character (Alice, Stitch, Belle): ")

# Logical Error: Using capitalize() on user input, which may lead to incorrect comparison
user_choice = user_choice.capitalize()

# Compilation Error 1: Incorrect assignment using '==' instead of '='
full_message == ""

# Runtime Error: NameError, undefined variable 'characterss'
if user_choice in characterss:
    if user_choice == "alice":
        full_message = "Alice is on a curious adventure."
    elif user_choice == "stitch":
        full_message = "Stitch is causing intergalactic mischief."
    else:
        full_message = "Belle is exploring a magical land."
# Compilation Error 2: IndentationError, incorrect indentation for the else statement
else:
full_message = "Invalid choice. Please choose from Alice, Stitch, or Belle."

print(full_message)


# CORRECT CODE:
# characters = ["Alice", "Stitch", "Belle"]
# user_choice = input("Choose a character (Alice, Stitch, Belle): ").capitalize()

# full_message = ""
# if user_choice in characters:
#     if user_choice == "Alice":
#         full_message = "Alice is on a curious adventure."
#     elif user_choice == "Stitch":
#         full_message = "Stitch is causing intergalactic mischief."
#     else:
#         full_message = "Belle is exploring a magical land."
# else:
#     full_message = "Invalid choice. Please choose from Alice, Stitch, or Belle."

# print(full_message)
