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

    def get_upcoming_birthdays(self, days: int):
        """
        Return a string with contacts who have birthdays in the given number of days.
        """
        today = date.today()
        result = []

        for record in self.data.values():
            if record.birthday:
                bday = record.birthday.date
                next_bday = bday.replace(year=today.year)
                if next_bday < today:
                    next_bday = next_bday.replace(year=today.year + 1)
                if 0 <= (next_bday - today).days <= days:
                    result.append(f"{record.name.value}: {next_bday.strftime('%d.%m.%Y')}")

        return "\n".join(result) if result else "No upcoming birthdays."

    def search(self, query: str):
        """
        Return a list of contacts whose name, email, or address contains the query string (case-insensitive).
        """
        result = []
        query_lower = query.lower()
        for record in self.data.values():
            name_match = query_lower in record.name.value.lower()
            address_match = query_lower in record.address.value.lower() if record.address else False
            email_match = any(query_lower in email.value.lower() for email in record.emails)
            if name_match or address_match or email_match:
                result.append(record)
        return result