"""
Field types for records: Name, Phone, Address, Email, Birthday.
"""

import re
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
    Phone field with Ukrainian phone number format validation.
    """
    def __init__(self, value: str):
        pattern = re.fullmatch(r"(\+?38)?0\d{9}$", value)
        if not pattern:
            raise ValueError("Invalid Ukrainian phone number format.")
        if value.startswith("0"):
            normalized = f"+38{value}"
        elif value.startswith("380"):
            normalized = f"+{value}"
        elif value.startswith("+380"):
            normalized = value
        else:
            raise ValueError("Unrecognized phone number format.")
        super().__init__(normalized)

class Address(Field):
    """Address field (no validation)."""
    pass

class Email(Field):
    """
    Email field with format validation.
    """
    def __init__(self, value: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email format.")
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
