"""
Field types for records: Name, Phone, Birthday.
"""

from datetime import datetime

class Field:
    """
    Base class for all fields.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Name field (no validation)."""
    pass

class Phone(Field):
    """
    Phone field with 10-digit validation.
    """
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Birthday(Field):
    """
    Birthday field in format DD.MM.YYYY.
    """
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)
