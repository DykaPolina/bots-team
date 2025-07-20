from src.models.address_book import AddressBook


def set_birthday(args, book: AddressBook):
    """
    Set a birthday to an existing contact.
    Usage: set-birthday [name] [DD.MM.YYYY]
    """
    if len(args) != 2:
        return "Usage: set-birthday [name] [DD.MM.YYYY]"
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
    if not record.birthday:
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
