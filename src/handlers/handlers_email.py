from src.models.address_book import AddressBook

def add_email(args, book: AddressBook):
    """
    Add an email to an existing contact.
    Usage: add-email [name] [email]
    """
    if len(args) != 2:
        return "Usage: add-email [name] [email]"
    name, email = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_email(email)
    return "Email added."


def change_email(args, book: AddressBook):
    """
    Change an email for an existing contact.
    Usage: change-email [name] [old_email] [new_email]
    """
    if len(args) != 3:
        return "Usage: change-email [name] [old_email] [new_email]"
    name, old_email, new_email = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    success = record.edit_email(old_email, new_email)
    return "Email updated." if success else "Old email not found."


def show_email(args, book: AddressBook):
    """
    Show all emails of a contact.
    Usage: show-email [name]
    """
    if len(args) != 1:
        return "Usage: show-email [name]"
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return record.get_emails() or "No emails saved."


def remove_email(args, book: AddressBook):
    """
    Remove an email from a contact.
    Usage: remove-email [name] [email]
    """
    if len(args) != 2:
        return "Usage: remove-email [name] [email]"
    name, email = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    if not record.find_email(email):
        return "Email not found."
    if not record.emails:
        return "The contact has no emails saved."
    record.remove_email(email)
    return "Email removed."


def find_email(args, book: AddressBook):
    """
    Find an email in a contact.
    Usage: find-email [name] [email]
    """
    if len(args) != 2:
        return "Usage: find-email [name] [email]"
    name, email = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    found = record.find_email(email)
    return f"Email found: {found.value}" if found else "Email not found."

