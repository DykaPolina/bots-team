from src.models.address_book import AddressBook

def set_address(args, book: AddressBook):
    """
    Set an address to an existing contact.
    Usage: set-address [name] [address]
    """
    if len(args) < 2:
        return "Usage: set-address [name] [address]"
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
