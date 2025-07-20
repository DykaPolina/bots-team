from src.models.record import Record
from src.models.address_book import AddressBook


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
        return "The contact has no phones saved."
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


