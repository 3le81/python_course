try:
    # Ask the user how many students are registering, with a limit of 20, to not crash the process
    num_students = int(
        input("How many students are registering? (Maximum 20) "))

    # Limit the number of students to 20
    num_students = min(num_students, 20)

    # Open the file in write mode (if file does not exist,it will be created with 'w' mode)
    with open('reg_form.txt', 'w') as file:
        # Iterate for each student
        for n in range(num_students):
            # Ask the user to enter the student ID
            student_id = input("Enter the student ID: ")

            # Write the student ID to the file
            file.write(f"{student_id}\n")

            # Write the ID student and a dotted line where student can sign up
            file.write('-' * 30 + '\n')

    # Provide a custom message indicating the completion of the registration process
    print(f"Registration completed. Student IDs have been saved to 'reg_form.txt'")

except ValueError:
    print("Error: Please enter a valid integer for the number of students.")

except PermissionError:
    print("Error: Unable to create or write to the file 'reg_form.txt'. Check permissions.")
