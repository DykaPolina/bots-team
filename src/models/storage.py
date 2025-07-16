import pickle
from src.models.address_book import AddressBook


def save_data(book, filename="src/data/addressbook.pkl"):
    """Save AddressBook to a file using pickle."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="src/data/addressbook.pkl"):
    """Load AddressBook from a file using pickle."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()