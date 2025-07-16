"""
Single contact record with name, phones, and optional birthday.
"""

from .fields import Name, Phone, Birthday

class Record:
    """
    Represents a single contact record.
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        """Add a phone number to the contact."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """Remove a phone number from the contact."""
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        """Replace an old phone number with a new one."""
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False

    def find_phone(self, phone):
        """Find and return a specific phone number."""
        return next((p for p in self.phones if p.value == phone), None)

    def add_birthday(self, birthday_str):
        """Add or update the birthday."""
        self.birthday = Birthday(birthday_str)

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        bday = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{bday}"

    def get_phones(self):
        """Return all phones as a string."""
        return "; ".join(p.value for p in self.phones)

    def get_birthday(self):
        """Return birthday value or None."""
        return self.birthday.value if self.birthday else None
