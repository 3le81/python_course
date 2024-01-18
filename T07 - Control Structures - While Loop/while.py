# Initialize variables to keep track of the total and count of numbers
total = 0
count = 0

# Continue taking input until -1 is entered
while True:
    # Get the user input
    user_input = input("Please enter a number (-1 to exit): ")

    # Check if the user wants to exit
    if user_input == '-1':
        # Check if any numbers were entered before exiting
        if count > 0:
            # Calculate the average by dividing the total by the count
            average = total / count
            # Print the average
            print("The average is:", average)
        else:
            print("No numbers entered.")

        # Exit the loop
        break

    # Check if the input consists of digits
    if user_input.isdigit():
        # Convert the input to an integer
        user_input = int(user_input)

        # Add the current input to the total
        total += user_input

        # Increment the count of numbers entered
        count += 1
    else:
        print("Invalid input. Please enter a valid number.")
