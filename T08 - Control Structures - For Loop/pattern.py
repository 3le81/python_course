# Initialize the stars variable with one star
stars = "*"

# Loop to print stars from 1 to 5 and then from 4 to 1
for i in range(9):
    # Print the current stars
    print(stars)

    # Adjust stars based on the current iteration
    if i < 4:
        # Add one more star for the first 4 iterations
        stars += "*"
    else:
        """ Remove one star for the remaining iterations,
        using a slicing notation to indicate that we want
        all the characters in the string except the last one."""
        stars = stars[:-1]

# tried with range(23) and the if i < 11 it's even nicer!