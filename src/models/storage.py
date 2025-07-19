import pickle
from src.models.address_book import AddressBook
from src.models.classNotes import Notes


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
    

def save_notes(notes, filename="src/data/notesbook.pkl"):
    """Save Notes to a file using pickle."""
    with open(filename, "wb") as file:
        pickle.dump(notes, file)

def load_notes(filename="src/data/notesbook.pkl"):
    """Load Notes from a file using pickle."""
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return Notes()
