import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.bots_team.models.record import Record


def test_add_and_find_phone():
    record = Record("Alice")
    record.add_phone("0501234567")
    found = record.find_phone("0501234567")
    assert found is not None
    assert found.value == "+380501234567"


def test_edit_phone_success():
    record = Record("Bob")
    record.add_phone("0501112233")
    success = record.edit_phone("0501112233", "0509998877")
    assert success is True
    assert record.find_phone("0501112233") is None
    assert record.find_phone("0509998877") is not None


def test_edit_phone_failure():
    record = Record("Charlie")
    record.add_phone("0500000000")
    success = record.edit_phone("0999999999", "0501111111")
    assert success is False


def test_remove_phone():
    record = Record("Diana")
    record.add_phone("0507654321")
    record.remove_phone("0507654321")
    assert record.find_phone("+380507654321") is None


def test_add_edit_remove_email():
    record = Record("Eve")
    record.add_email("eve@example.com")
    assert record.get_emails() == "eve@example.com"

    record.edit_email("eve@example.com", "new@example.com")
    assert record.get_emails() == "new@example.com"

    record.remove_email("new@example.com")
    assert record.get_emails() == ""


def test_set_and_remove_address():
    record = Record("Frank")
    record.set_address("Kyiv, Ukraine")
    assert record.get_address() == "Kyiv, Ukraine"

    record.remove_address()
    assert record.get_address() is None


def test_set_and_remove_birthday():
    record = Record("Hanna")
    record.set_birthday("01.01.2000")
    assert record.get_birthday() == "01.01.2000"

    record.remove_birthday()
    assert record.get_birthday() is None


def test_str_representation():
    record = Record("Ivan")
    record.add_phone("0501112233")
    record.set_address("Lviv")
    record.add_email("ivan@example.com")
    record.set_birthday("05.05.1995")

    result = str(record)
    assert "Ivan" in result
    assert "+380501112233" in result
    assert "Lviv" in result
    assert "ivan@example.com" in result
    assert "05.05.1995" in result
