def display_menu():
    print("\nMenu Options:")
    print("0 - Exit Program")
    print("1 - Look Up an Email Address")
    print("2 - Add a New Contact")
    print("3 - Update an Existing Contact")
    print("4 - Remove a Contact")
    print("5 - Display All Contacts")

def email_directory():
    contacts = {}

    while True:
        display_menu()
        choice = input("\nEnter your choice > ")

        if choice == '0':
            print("Goodbye!")
            break
        elif choice == '1':
            name = input("Enter the name: ")
            print(f"The email address is {contacts.get(name, 'not found.')}")
        elif choice == '2':
            name = input("Enter the name: ")
            email = input("Enter the email: ")
            contacts[name] = email
            print(f"Contact added: {contacts}")
        elif choice == '3':
            name = input("Enter the name to update: ")
            if name in contacts:
                email = input("Enter the new email: ")
                contacts[name] = email
                print("Contact updated.")
            else:
                print("Contact not found.")
        elif choice == '4':
            name = input("Enter the name to remove: ")
            if contacts.pop(name, None):
                print("Contact removed.")
            else:
                print("Contact not found.")
        elif choice == '5':
            print("\nAll Contacts:")
            for name, email in contacts.items():
                print(f"{name}: {email}")
        else:
            print("Invalid choice. Try again.")

email_directory()
