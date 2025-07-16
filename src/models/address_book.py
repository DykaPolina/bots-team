"""
Custom dictionary to store and manage contact records.
"""

from collections import UserDict
from datetime import date

class AddressBook(UserDict):
    """
    Class representing an address book.
    """

    def add_record(self, record):
        """Add a new record to the address book."""
        self.data[record.name.value] = record

    def find(self, name):
        """Find a record by contact name."""
        return self.data.get(name)

    def delete(self, name):
        """Delete a record by contact name."""
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        """
        Return a string with contacts who have birthdays in the next 7 days.
        """
        today = date.today()
        result = []

        for record in self.data.values():
            if record.birthday:
                bday = record.birthday.date
                next_bday = bday.replace(year=today.year)
                if next_bday < today:
                    next_bday = next_bday.replace(year=today.year + 1)
                if 0 <= (next_bday - today).days <= 7:
                    result.append(f"{record.name.value}: {next_bday.strftime('%d.%m.%Y')}")

        return "\n".join(result) if result else "No upcoming birthdays."
