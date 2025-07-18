"""
Handlers for each bot command.
"""

from .utils import input_error
from src.models.record import Record


@input_error
def add_contact(args, book):
    """
    Add a new contact or phones to an existing one.
    Usage: add [name] [phone1] [phone2] ...
    """
    if len(args) < 2:
        return "Usage: add [name] [phone1] [phone2] ..."
    name, *phones = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    for phone in phones:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    """
    Change a phone number for an existing contact.
    Usage: change [name] [old_phone] [new_phone]
    """
    if len(args) != 3:
        return "Usage: change [name] [old_phone] [new_phone]"
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    success = record.edit_phone(old_phone, new_phone)
    return "Phone updated." if success else "Old phone number not found."


@input_error
def show_phone(args, book):
    """
    Show all phone numbers of a contact.
    Usage: phone [name]
    """
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return record.get_phones() or "No phone numbers saved."


def show_all(book, args=None):
    """
    Show all records in the address book.
    Usage: all
    """
    if args:
        return "Usage: all"
    if not book.data:
        return "No contacts found."
    return "\n".join(str(record) for record in book.values())

@input_error
def set_address(args, book):
    """
    Set an address to an existing contact.
    Usage: add-address [name] [address]
    """
    if len(args) < 2:
        return "Usage: add-address [name] [address]"
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.set_address(address)
    return "Address added."

@input_error
def show_address(args, book):
    """
    Show the address of a contact.
    Usage: show-address [name]
    """
    if len(args) != 1:
        return "Usage: show-address [name]"
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return record.get_address() or "No address saved."

@input_error
def remove_address(args, book):
    """
    Remove an address from a contact.
    Usage: remove-address [name]
    """
    if len(args) != 1:
        return "Usage: remove-address [name]"
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    if not record.address():
        return "The contact has no address saved."
    record.remove_address()
    return "Address removed."

@input_error
def add_email(args, book):
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

@input_error
def change_email(args, book):
    """
    Change an email for an existing contact.
    Usage: change-email [name] [old_email] [new_email]
    """
    if len(args) != 3:
        return "Usage: change [name] [old_email] [new_email]"
    name, old_email, new_email = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    success = record.edit_email(old_email, new_email)
    return "Email updated." if success else "Old email not found."

@input_error
def show_email(args, book):
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

@input_error
def remove_email(args, book):
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

@input_error
def find_email(args, book):
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

@input_error
def set_birthday(args, book):
    """
    Set a birthday to an existing contact.
    Usage: add-birthday [name] [DD.MM.YYYY]
    """
    if len(args) != 2:
        return "Usage: add-birthday [name] [DD.MM.YYYY]"
    name, bday = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.set_birthday(bday)
    return "Birthday added."


@input_error
def show_birthday(args, book):
    """
    Show the birthday of a contact.
    Usage: show-birthday [name]
    """
    if len(args) != 1:
        return "Usage: show-birthday [name]"
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return record.get_birthday() or "No birthday saved."

@input_error
def remove_birthday(args, book):
    """
    Remove a birthday from a contact.
    Usage: remove-birthday [name]
    """
    if len(args) != 1:
        return "Usage: remove-birthday [name]"
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    if not record.birthday():
        return "The contact has no birthday saved."
    record.remove_birthday()
    return "Birthday removed."

@input_error
def birthdays(args, book):
    """
    Call the address book method to get upcoming birthdays.
    Usage: birthdays [days]
    """
    if len(args) != 1:
        return "Usage: birthdays [days]"
    days = args[0]
    return book.get_upcoming_birthdays(int(days))


@input_error
def remove_phone(args, book):
    """
    Remove a phone number from a contact.
    Usage: remove-phone [name] [phone]
    """
    if len(args) != 2:
        return "Usage: remove-phone [name] [phone]"
    name, phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    if not record.find_phone(phone):
        return "Phone number not found."
    if not record.phones:
        return "The contact has no emails saved."
    record.remove_phone(phone)
    return "Phone removed."


@input_error
def find_phone(args, book):
    """
    Find a phone number in a contact.
    Usage: find-phone [name] [phone]
    """
    if len(args) != 2:
        return "Usage: find-phone [name] [phone]"
    name, phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    found = record.find_phone(phone)
    return f"Phone found: {found.value}" if found else "Phone not found."


@input_error
def delete_contact(args, book):
    """
    Delete a contact completely.
    Usage: delete-contact [name]
    """
    if len(args) != 1:
        return "Usage: delete-contact [name]"
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    book.delete(name)
    return "Contact deleted."

@input_error
def search(args, book):
    """
    Search for contacts by name, email, or address.
    Usage: search [query]
    """
    if len(args) != 1:
        return "Usage: search [query]"
    query = args[0]
    results = book.search(query)
    if not results:
        return "No matching contacts found."
    return "\n".join(str(record) for record in results)

def help_command(args, book):
    """
    Show available commands and usage.
    Usage: help
    """
    if args:
        return "Usage: help"
    return (
        "Available commands:\n"
        "  hello                         - Greet the bot\n"
        "  add [name] [phones...]        - Add contact with one or more phone numbers\n"
        "  change [name] [old] [new]     - Replace old phone with new\n"
        "  phone [name]                  - Show contact's phones\n"
        "  all                           - Show all contacts\n"
        "  set-birthday [name] [date]    - Set birthday in DD.MM.YYYY format\n"
        "  show-birthday [name]          - Show birthday of contact\n"
        "  birthdays [days]              - Show upcoming birthdays in the given number of days\n"
        "  remove-phone [name] [phone]   - Remove a phone number\n"
        "  find-phone [name] [phone]     - Check if phone exists\n"
        "  delete-contact [name]         - Remove the entire contact\n"
        "  help                          - Show this help message\n"
        "  close / exit                  - Exit the program"
    )
