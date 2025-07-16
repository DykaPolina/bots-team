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
    return record.get_phones()


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
    return record.get_birthday() or "No birthday set."


@input_error
def birthdays(args, book):
    """
    Call the address book method to get upcoming birthdays.
    Usage: birthdays
    """
    if args:
        return "Usage: birthdays"
    return book.get_upcoming_birthdays()


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
