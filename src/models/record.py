"""
Single contact record with name, phones, and optional address, emails, birthday.
"""

from .fields import Name, Phone, Address, Email, Birthday

class Record:
    """
    Represents a single contact record.
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = None
        self.emails = []
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

    def set_address(self, address: str):
        """Add or update the address."""
        self.address = Address(address)

    def remove_address(self):
        """Delete the address."""
        self.address = None

    def add_email(self, email: str):
        """Add an email to the contact list of emails."""
        self.emails.append(Email(email))

    def remove_email(self, email: str):
        """Delete an email from the contact list of emails."""
        self.emails = [e for e in self.emails if e.value != email]

    def edit_email(self, old_email: str, new_email: str):
        """Replace an old email with a new one."""
        for i, e in enumerate(self.emails):
            if e.value == old_email:
                self.emails[i] = Email(new_email)
                return True
        return False

    def set_birthday(self, birthday_str):
        """Add or update the birthday."""
        self.birthday = Birthday(birthday_str)

    def remove_birthday(self):
        """Delete the birthday."""
        self.birthday = None

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        address = f", address: {self.address.value}" if self.address else ""
        emails = f", emails: {"; ".join(e.value for e in self.emails)}" if self.emails else ""
        bday = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{address}{emails}{bday}"

    def get_phones(self):
        """Return all phones as a string."""
        return "; ".join(p.value for p in self.phones)

    def get_address(self):
        """Return address value or None."""
        return self.address.value if self.address else None
    
    def get_emails(self):
        """Return all emails as a string."""
        return "; ".join(e.value for e in self.emails)

    def get_birthday(self):
        """Return birthday value or None."""
        return self.birthday.value if self.birthday else None
