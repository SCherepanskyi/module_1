import os
from typing import NoReturn, List, Tuple, Optional

USER_CONTACTS_FILE = "user_contacts.txt"


def validate_phone(phone: str) -> bool:
    """Check if phone is valid."""
    return phone.isdigit() and len(phone) == 12


def validate_email(email: str) -> bool:
    """Check if email is valid."""
    return '@' in email and '.' in email.split('@')[1]


def add_contact() -> None:
    """Add new contact to contacts file."""
    while True:
        name: str = input("Please enter a name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue

        phone: str = input("Please enter a phone number (12 digits): ").strip()
        if not validate_phone(phone):
            print("Invalid phone number. Phone number must be 12 digits.")
            continue

        email: str = input("Please enter an email: ").strip()
        if not validate_email(email):
            print("Invalid email. Email must contain @ and .")
            continue

        with open(USER_CONTACTS_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{name},{phone},{email}\n")
        print("Contact successfully added!")
        break


def find_contact() -> None:
    """Find contact by name or phone number."""
    search_term: str = input("Enter a name or phone number to search: ").strip().lower()
    found: bool = False

    if not os.path.exists(USER_CONTACTS_FILE):
        print("Contact not found.")
        return

    with open(USER_CONTACTS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            name, phone, email = line.strip().split(',')
            if search_term in name.lower() or search_term in phone:
                print(f"Name: {name}, Phone: {phone}, Email: {email}")
                found = True

    if not found:
        print("Contact not found.")


def delete_contact() -> None:
    """Delete contact by name or phone number."""
    search_term: str = input("Please enter a name or phone number to delete: ").strip().lower()
    found: bool = False
    contacts: List[str] = []

    if not os.path.exists(USER_CONTACTS_FILE):
        print("Contact not found.")
        return

    with open(USER_CONTACTS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            name, phone, email = line.strip().split(',')
            if search_term in name.lower() or search_term in phone:
                found = True
            else:
                contacts.append(line)

    if found:
        with open(USER_CONTACTS_FILE, 'w', encoding='utf-8') as f:
            f.writelines(contacts)
        print("Contact deleted!")
    else:
        print("Contact not found.")


def update_contact() -> None:
    """Update existing contact by name or phone number."""
    search_term: str = input("Please enter a name or phone number to update: ").strip().lower()
    found: bool = False
    contacts: List[str] = []
    updated_contact: Optional[str] = None

    if not os.path.exists(USER_CONTACTS_FILE):
        print("Contact not found.")
        return

    with open(USER_CONTACTS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            name, phone, email = line.strip().split(',')
            if search_term in name.lower() or search_term in phone:
                found = True
                print(f"Contact found: Name: {name}, Phone: {phone}, Email: {email}")

                while True:
                    new_name: str = input("Please enter a new name (leave blank to keep unchanged): ").strip()
                    new_phone: str = input(
                        "Please enter a phone number (12 digits, leave blank to keep unchanged): ").strip()
                    new_email: str = input("Please enter a new email (leave blank to keep unchanged): ").strip()

                    if new_name:
                        name = new_name
                    if new_phone:
                        if not validate_phone(new_phone):
                            print("Invalid phone number. Phone number must be 12 digits.")
                            continue
                        phone = new_phone
                    if new_email:
                        if not validate_email(new_email):
                            print("Invalid email. Email must contain @ and .")
                            continue
                        email = new_email

                    updated_contact = f"{name},{phone},{email}\n"
                    contacts.append(updated_contact)
                    break
            else:
                contacts.append(line)

    if found:
        with open(USER_CONTACTS_FILE, 'w', encoding='utf-8') as f:
            f.writelines(contacts)
        print("Contact updated!")
    else:
        print("Contact not found.")


def view_contacts() -> None:
    """View all contacts in contacts file sorted by name."""
    if not os.path.exists(USER_CONTACTS_FILE):
        print("List of contacts is empty.")
        return

    with open(USER_CONTACTS_FILE, 'r', encoding='utf-8') as f:
        contacts: List[Tuple[str, str, str]] = [line.strip().split(',') for line in f]

    if not contacts:
        print("List of contacts is empty.")
        return

    contacts.sort(key=lambda x: x[0].lower())
    print("\nList of contacts (sorted by name): ")
    for name, phone, email in contacts:
        print(f"Name: {name}, Phone: {phone}, Email: {email}")


def main() -> NoReturn:
    """Main function to run the program."""
    print("Welcome to the Contacts Manager!")

    while True:
        print("\nPlease choose an option:")
        print("1. Add contact")
        print("2. Find contact by name or phone number")
        print("3. Delete contact by name or phone number")
        print("4. Update contact by name or phone number")
        print("5. View contacts")
        print("6. Exit")

        choice: str = input("Your choice: ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            find_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            view_contacts()
        elif choice == '6':
            print("The program has been completed. Bye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()