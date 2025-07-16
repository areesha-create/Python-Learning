class ContactManager:
    def __init__(self, file_name):
        self.file = file_name

    def add_contact(self, name, email, relation, age):
        with open(self.file, 'a') as f:
            f.write(f"{name},{email},{relation},{age}\n")
        print(f"Added {name}.")

    def view_contacts(self):
        try:
            with open(self.file, 'r') as f:
                contacts = f.readlines()
            if not contacts:
                print("No contacts.")
            else:
                print("--- Contacts ---")
                for c in contacts: 
                    print(c.strip())
        except FileNotFoundError:
            print("No contact file.")

if __name__ == "__main__":
    my_contacts = ContactManager("my_contacts.txt")

    print("Adding contacts...")
    my_contacts.add_contact("Rukhsana", "rukhsana@gmail.com", "Family", 43)
    my_contacts.add_contact("Fatima Khan", "fatima@gmail.com", "Family", 21)

    my_contacts.view_contacts()
