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
        # Remove one star for the remaining iterations
        # Using slicing notation to remove the last character
        stars = stars[:-1]


# I tried with range(23) and found that if i < 11, it's even nicer!
