import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from bots_team.models.fields import Phone, Email, Birthday


@pytest.mark.parametrize("input_number,expected", [
    ("0501234567", "+380501234567"),
    ("380501234567", "+380501234567"),
    ("+380501234567", "+380501234567"),
])
def test_valid_phone_formats(input_number, expected):
    phone = Phone(input_number)
    assert phone.value == expected


@pytest.mark.parametrize("invalid_number", [
    "12345", "38050123456", "+390501234567", "050123456", "501234567", "abc"
])
def test_invalid_phone_raises(invalid_number):
    with pytest.raises(ValueError, match="Invalid Ukrainian phone number format."):
        Phone(invalid_number)


@pytest.mark.parametrize("valid_email", [
    "test@example.com",
    "user.name@domain.co",
    "u@d.com",
])
def test_valid_email(valid_email):
    email = Email(valid_email)
    assert email.value == valid_email


@pytest.mark.parametrize("invalid_email", [
    "plainaddress",
    "@missinguser.com",
    "user@.com",
    "user@com",
    "user@domain,com",
])
def test_invalid_email_raises(invalid_email):
    with pytest.raises(ValueError, match="Invalid email format."):
        Email(invalid_email)


def test_valid_birthday():
    birthday = Birthday("01.01.2000")
    assert birthday.value == "01.01.2000"
    assert birthday.date.year == 2000


def test_invalid_birthday_format():
    with pytest.raises(ValueError, match="Invalid date format. Use DD.MM.YYYY"):
        Birthday("2000-01-01")

