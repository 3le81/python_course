# Initialize variables to keep track of the total and count of numbers
total = 0
count = 0

# Get the first number (integer chosen from user input)
user_input = int(input("Please enter a number (-1 to exit): "))

# Continue taking input until -1 is entered
while user_input != -1:
    # Add the current input to the total
    total += user_input

    # Increment the count of numbers entered
    count += 1

    # Get the next user input
    user_input = int(input("Please enter a number (-1 to exit): "))

    # Check if the user wants to exit
    if user_input == -1:
        # Calculate the average by dividing the total by the count
        average = total / count
     # Print the average
        print("The average is:", average)
        
        # Exit the loop
        break
