# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Logical error: missing quotation marks around "Lion"
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# Logical error: incorrect placement of variables in the string, and missing f-string or .format()
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

# Syntax error: missing parentheses in the print statement
print(full_spec)
