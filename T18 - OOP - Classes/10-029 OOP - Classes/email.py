### --- OOP Email Simulator --- ###

# --- Email Class --- #

# Create the class, constructor and methods to create a new Email object.
class Email:
    # Class variable with default value
    has_been_read = False

    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []


# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add them to the Inbox list.
    inbox.append(Email("sender1@example.com",
                 "Welcome to HyperionDev!", "Thank you for joining."))
    inbox.append(Email("sender2@example.com",
                 "Great work on the bootcamp!", "Keep up the good work."))
    inbox.append(Email("sender3@example.com", "Your excellent marks!",
                 "Congratulations on your achievements."))


def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for index, email in enumerate(inbox):
        print(f"{index} {email.subject_line}")


def read_email(index):
    # Create a function which displays a selected email.
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(
            f"\nEmail from {email.email_address} - Subject: {email.subject_line}\n")
        print(email.email_content)
        email.mark_as_read()
        print("\nEmail marked as read.\n")
    else:
        print("Invalid index. Please choose a valid email.")


# --- Email Program --- #
# Call the function to populate the Inbox for further use.
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while menu:
    # try-except block around the user input to catch ValueError if the input is not a valid integer
    try:
        user_choice = int(input('''\nWould you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: '''))

        if user_choice == 1:
            # Logic to read an email
            list_emails()
            index_to_read = int(
                input("Enter the number of the email you want to read: "))
            read_email(index_to_read)

        elif user_choice == 2:
            # Logic to view unread emails
            unread_emails = [
                email.subject_line for email in inbox if not email.has_been_read]
            if unread_emails:
                print("\nUnread Emails:")
                for subject_line in unread_emails:
                    print(subject_line)
            else:
                print("\nNo unread emails.")

        elif user_choice == 3:
            # Logic to exit the application
            print("Quitting application. Have a great day!")
            menu = False

        else:
            print("Oops - incorrect input.")

    except ValueError:
        print("Invalid input. Please enter a number.")
