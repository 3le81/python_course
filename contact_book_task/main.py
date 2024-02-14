"""
Create a contact list manager

contacts 
-name
-email
-cell number

Add contact
Remove contact
View contacts
Sort contacts


Contacts should be saved to textfile and retrieved when starting program
"""
import os
from tabulate import tabulate
from contacts import Contact, ContactList


# Function to clear the console screen

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_welcome_message():
    print("*" * 30)
    print("WELCOME TO THE CONTACT LIST MANAGER!")
    print("*" * 30)


def print_menu():
    print("\nContact List Manager\n")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. View Contacts")
    print("4. Sort Contacts")
    print("5. Exit")


def add_contact(contact_list, contacts_file):
    name = input("Enter name: ")
    email = input("Enter email: ")
    cell_number = input("Enter cell number: ")
    contact_list.add_contact(Contact(name, email, cell_number))
    contact_list.save_to_file(contacts_file)
    print("Contact added successfully.")


def remove_contact(contact_list, contacts_file):
    if not contact_list.contacts:
        print("No contacts to remove.")
        return
    print("Contacts:")
    contact_table = [["Index", "Name"]]
    for contact_index, contact in enumerate(contact_list.contacts):
        contact_table.append([contact_index + 1, contact.name])
    print(tabulate(contact_table, headers="firstrow", tablefmt="grid"))
    try:
        selected_index = int(input("Enter index of contact to remove: ")) - 1
        if 0 <= selected_index < len(contact_list.contacts):
            contact_list.remove_contact(selected_index)
            contact_list.save_to_file(contacts_file)
            print("Contact removed successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def main():
    contacts_file = "contacts.txt"
    contact_list = ContactList()
    contact_list.load_from_file(contacts_file)

    clear_screen()
    print_welcome_message()

    while True:
        print_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contact_list, contacts_file)

        elif choice == "2":
            remove_contact(contact_list, contacts_file)

        elif choice == "3":
            contact_list.display_contacts()

        elif choice == "4":
            if not contact_list.contacts:
                print("No contacts to sort.")
            else:
                contact_list.sort_contacts()
                print("Contacts sorted.")
                contact_list.display_contacts()

        elif choice == "5":
            print("\nExiting program. GOODBYE!")
            print("*" * 30)
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
