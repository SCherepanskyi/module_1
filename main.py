import os
from typing import NoReturn, List, Tuple, Optional

USER_CONTACTS_FILE = "user_contacts.txt"

def validate_name() -> str:
    """Check if name is valid."""
    while True:
        try:
            name: str = input("Please enter a name: ").strip()
            if not name:
                raise ValueError('Name cannot be empty.')
            return name
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def validate_phone() -> str:
    """Check if phone is valid."""
    while True:
        try:
            phone: str = input("Please enter a phone number (12 digits): ").strip()
            if not phone.isdigit() or len(phone) != 12:
                raise ValueError('Phone number must be 12 digits.')
            return phone
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def validate_email() -> str:
    """Check if email is valid."""
    while True:
        try:
            email: str = input("Please enter an email: ").strip()
            if '@' not in email or '.' not in email.split('@')[1]:
                raise ValueError('Email must contain @ and .')
            return email
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def validate_search_term() -> str:
    """Check if search term is valid."""
    while True:
        try:
            term: str = input("Enter a name or phone number to search: ").strip().lower()
            if not term:
                raise ValueError('Search term cannot be empty.')
            return term
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def read_contacts() -> List[Tuple[str, str, str]]:
    """Reads all contacts from contacts file and returns them as a list."""
    contacts: List[Tuple[str, str, str]] = []

    if not os.path.exists(USER_CONTACTS_FILE):
        return []

    with open(USER_CONTACTS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            name, phone, email = line.strip().split(',')
            contacts.append((name, phone, email))
    return contacts

def write_contacts(contacts: List[Tuple[str, str, str]]) -> None:
    """Writes contacts to contacts file."""
    with open(USER_CONTACTS_FILE, 'w', encoding='utf-8') as f:
        for name, phone, email in contacts:
            f.write(f"{name},{phone},{email}\n")

def add_contact() -> None:
    """Add new contact to contacts file."""
    name = validate_name()
    phone = validate_phone()
    email = validate_email()

    contacts: List[Tuple[str, str, str]] = read_contacts()
    contacts.append((name, phone, email))

    write_contacts(contacts)
    print("Contact successfully added!")

def find_contact() -> None:
    """Find contact by name or phone number."""
    search_term = validate_search_term()
    found: bool = False
    contacts: List[Tuple[str, str, str]] = read_contacts()

    for name, phone, email in contacts:
        if search_term in name.lower() or search_term in phone:
            print(f"Contact found: Name: {name}, Phone: {phone}, Email: {email}")
            found = True

    if not found:
        print("Contact not found.")

def delete_contact() -> None:
    """Delete contact by name or phone number."""
    search_term = validate_search_term()

    contacts: List[Tuple[str, str, str]] = read_contacts()
    new_contacts: List[Tuple[str, str, str]] = []
    found: bool = False

    for contact in contacts:
        name, phone, email = contact
        if search_term in name.lower() or search_term in phone:
            found = True
        else:
            new_contacts.append(contact)

    if found:
        write_contacts(new_contacts)
        print("Contact deleted!")
    else:
        print("Contact not found.")

def update_contact() -> None:
    """Update existing contact by name or phone number."""
    search_term = validate_search_term()
    contacts: List[Tuple[str, str, str]] = read_contacts()
    updated: bool = False

    for i, (name, phone, email) in enumerate(contacts):
        if search_term in name.lower() or search_term in phone:
            print(f"Contact found: Name: {name}, Phone: {phone}, Email: {email}")

            new_name = validate_name() if input("Would you like to change a name? (y/n): ").strip().lower() == 'y' else name
            new_phone = validate_phone() if input("Would you like to change a phone number? (y/n): ").strip().lower() == 'y' else phone
            new_email = validate_email() if input("Would you like to change an email? (y/n): ").strip().lower() == 'y' else email

            contacts[i] = (new_name, new_phone, new_email)
            updated = True
            break

    if updated:
        write_contacts(contacts)
        print("Contact updated!")
    else:
        print("Contact not found.")

def view_contacts() -> None:
    """View all contacts in contacts file sorted by name."""
    contacts: List[Tuple[str, str, str]] = read_contacts()

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