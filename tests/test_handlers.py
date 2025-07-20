import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from bots_team.models.address_book import AddressBook
from bots_team.models.notes import Notes
from bots_team.handlers.handlers import command_handler


@pytest.fixture
def book():
    return AddressBook()

@pytest.fixture
def notes():
    return Notes()


def test_add_contact_and_show_phone(book, notes):
    result = command_handler("add", book, ["Alice", "0501234567"], notes)
    assert result == "Contact added."

    result = command_handler("phone", book, ["Alice"], notes)
    assert "+380501234567" in result


def test_change_contact_phone(book, notes):
    command_handler("add", book, ["Bob", "0501112233"], notes)
    result = command_handler("change", book, ["Bob", "0501112233", "0509998877"], notes)
    assert result == "Phone updated."

    phone = command_handler("phone", book, ["Bob"], notes)
    assert "+380509998877" in phone


def test_set_and_show_address(book, notes):
    command_handler("add", book, ["Carol", "0501111222"], notes)
    result = command_handler("set-address", book, ["Carol", "Kyiv"], notes)
    assert result == "Address added."

    result = command_handler("show-address", book, ["Carol"], notes)
    assert result == "Kyiv"


def test_add_and_find_email(book, notes):
    command_handler("add", book, ["Dana", "0500000000"], notes)
    command_handler("add-email", book, ["Dana", "dana@example.com"], notes)
    result = command_handler("find-email", book, ["Dana", "dana@example.com"], notes)
    assert "dana@example.com" in result


def test_set_and_show_birthday(book, notes):
    command_handler("add", book, ["Eva", "0502223344"], notes)
    command_handler("set-birthday", book, ["Eva", "01.01.2000"], notes)
    result = command_handler("show-birthday", book, ["Eva"], notes)
    assert result == "01.01.2000"


def test_delete_contact(book, notes):
    command_handler("add", book, ["Fred", "0509990000"], notes)
    result = command_handler("delete-contact", book, ["Fred"], notes)
    assert result == "Contact deleted."

    result = command_handler("phone", book, ["Fred"], notes)
    assert result == "Contact not found."



def test_add_and_find_note(notes, book):
    result = command_handler("add-note", book, ["Buy", "milk"], notes)
    assert result == "Buy milk note added successfully"

    result = command_handler("find-all-note", book, [], notes)
    assert "Buy milk" in result


def test_edit_and_delete_note(notes, book):
    command_handler("add-note", book, ["Old", "note"], notes)
    result = command_handler("edit-note", book, ["Old note; New note"], notes)
    assert result == "Old note note edited successfully"

    result = command_handler("delete-note", book, ["New", "note"], notes)
    assert result == "New note note deleted successfully"


def test_find_text_in_note(notes, book):
    command_handler("add-note", book, ["Call", "Pasha"], notes)
    result = command_handler("find-text-in-note", book, ["Pasha"], notes)
    assert "Call Pasha" in result
