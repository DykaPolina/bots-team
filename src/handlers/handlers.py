"""
Handlers for each bot command.
"""

from .utils import input_error, execute_command
from src.models.record import Record
from src.models.classNotes import Notes
from src.models.address_book import AddressBook
from src.models.storage import save_data

def get_available_commands():
    return list(command_list.keys())


def command_hello():
    return "How can I help you?"


def add_contact(args, book: AddressBook):
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


def change_contact(args, book: AddressBook):
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


def show_phone(args, book: AddressBook):
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


def show_all(args, book: AddressBook):
    """
    Show all records in the address book.
    Usage: all
    """
    if args:
        return "Usage: all"
    if not book.data:
        return "No contacts found."
    return "\n".join(str(record) for record in book.values())


def set_address(args, book: AddressBook):
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


def show_address(args, book: AddressBook):
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


def remove_address(args, book: AddressBook):
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
        return "Usage: change [name] [old_email] [new_email]"
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


def set_birthday(args, book: AddressBook):
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


def show_birthday(args, book: AddressBook):
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


def remove_birthday(args, book: AddressBook):
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


def birthdays(args, book: AddressBook):
    """
    Call the address book method to get upcoming birthdays.
    Usage: birthdays [days]
    """
    if len(args) != 1:
        return "Usage: birthdays [days]"
    days = args[0]
    return book.get_upcoming_birthdays(int(days))


def remove_phone(args, book: AddressBook):
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


def find_phone(args, book: AddressBook):
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


def delete_contact(args, book: AddressBook):
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


def help_command(args=None):
    """
    Show available commands and usage.
    Usage: help
    """
    if args:
        return "Usage: help"
    return (
        "Available commands:\n"
        "  hello                          - Greet the bot\n"
        "  add [name] [phones...]         - Add contact with one or more phone numbers\n"
        "  change [name] [old] [new]      - Replace old phone with new\n"
        "  phone [name]                   - Show contact's phone numbers\n"
        "  all                            - Show all contacts\n"
        "  delete-contact [name]          - Remove the entire contact\n"
        "  search [query]                 - Search contacts by name, email, or address\n"
        "\n"
        "Address:\n"
        "  set-address [name] [address]   - Set or update address\n"
        "  show-address [name]            - Show contact's address\n"
        "  remove-address [name]          - Remove contact's address\n"
        "\n"
        "Email:\n"
        "  add-email [name] [email]       - Add email to contact\n"
        "  change-email [name] [old] [new]- Change email\n"
        "  show-email [name]              - Show all emails\n"
        "  remove-email [name] [email]    - Remove specific email\n"
        "  find-email [name] [email]      - Find specific email\n"
        "\n"
        "Birthday:\n"
        "  set-birthday [name] [DD.MM.YYYY] - Set birthday\n"
        "  show-birthday [name]           - Show birthday\n"
        "  remove-birthday [name]         - Remove birthday\n"
        "  birthdays [days]               - Show upcoming birthdays within days\n"
        "\n"
        "Phone (additional):\n"
        "  remove-phone [name] [phone]    - Remove specific phone number\n"
        "  find-phone [name] [phone]      - Find specific phone number\n"
        "\n"
        "Notes:\n"
        "  add-note [text]                - Add a note\n"
        "  edit-note [old]; [new]         - Edit a note (separate old and new by semicolon)\n"
        "  delete-note [text]             - Delete a note\n"
        "  find-all-note                  - Show all notes\n"
        "  find-text-in-note [text]       - Find notes containing text\n"
        "\n"
        "System:\n"
        "  help                           - Show this help message\n"
        "  close / exit                   - Exit the assistant\n"
    )


def command_exit(book: AddressBook):
    save_data(book)
    raise SystemExit("Good bye!")


def note_format(args):
        return " ".join(args)


def command_add_note(args, notes: Notes):
    note = note_format(args)
    return notes.add_note(note)


def command_edit_note(args, notes: Notes):
    note, new_note = note_format(args).split(";")
    return notes.edit_note(note, new_note.lstrip())


def command_find_all_note(notes: Notes):
    return notes.find_all_note()


def command_delete_note(args, notes: Notes):
    note = note_format(args)
    return notes.delete_note(note)


def command_find_text_in_note(args, notes: Notes):
    text = note_format(args)
    return notes.find_text_in_note(text)


command_list = {
        "hello": command_hello,

        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,

        "set-address": set_address,
        "show-address": show_address,
        "remove-address": remove_address,

        "add-email": add_email,
        "change-email": change_email,
        "show-email": show_email,
        "remove-email": remove_email,
        "find-email": find_email,

        "set-birthday": set_birthday,
        "show-birthday": show_birthday,
        "remove-birthday": remove_birthday,
        "birthdays": birthdays,

        "remove-phone": remove_phone,
        "find-phone": find_phone,
        "delete-contact": delete_contact,

        "help": help_command,
        "exit": command_exit,
        "close": command_exit,

        "add-note": command_add_note,
        "edit-note": command_edit_note,
        "find-all-note": command_find_all_note,
        "delete-note": command_delete_note,
        "find-text-in-note": command_find_text_in_note,

    }


@input_error
def command_hindler(command, book, args, notes):
    return execute_command(command_list[command], {"book": book, "args": args, "notes": notes})
    