from tabulate import tabulate


class Contact:
    def __init__(self, name="", email="", cell_number=""):
        self.name = name
        self.email = email
        self.cell_number = cell_number


class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, index):
        del self.contacts[index]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for contact in self.contacts:
                file.write(
                    f"{contact.name},{contact.email},{contact.cell_number}\n")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    name, email, cell_number = line.strip().split(',')
                    self.add_contact(Contact(name, email, cell_number))
        except FileNotFoundError:
            # If the file doesn't exist, create it
            open(filename, 'w').close()

    def display_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            table = [["Name", "Email", "Cell Number"]]
            for contact in self.contacts:
                table.append(
                    [contact.name, contact.email, contact.cell_number])
            print(tabulate(table, headers="firstrow", tablefmt="grid"))

    def sort_contacts(self):
        self.contacts.sort(key=lambda x: x.name)
