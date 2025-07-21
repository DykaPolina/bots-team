import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bots_team.models.notes import Notes


def test_add_note_success():
    notes = Notes()
    result = notes.add_note("Test note")
    assert result == "Test note note added successfully"
    assert notes.find_note("Test note").note == "Test note"

def test_add_note_duplicate():
    notes = Notes()
    notes.add_note("Test note")
    with pytest.raises(Exception, match="Note already exist"):
        notes.add_note("Test note")

def test_delete_note_success():
    notes = Notes()
    notes.add_note("To be deleted")
    result = notes.delete_note("To be deleted")
    assert result == "To be deleted note deleted successfully"
    assert notes.find_note("To be deleted") is None

def test_delete_note_not_exist():
    notes = Notes()
    with pytest.raises(Exception, match="Note does not exist"):
        notes.delete_note("Ghost")

def test_edit_note_success():
    notes = Notes()
    notes.add_note("Original")
    result = notes.edit_note("Original", "Updated")
    assert result == "Original note edited successfully"
    assert notes.find_note("Original") is None
    assert notes.find_note("Updated").note == "Updated"

def test_find_text_in_note():
    notes = Notes()
    notes.add_note("shopping list: milk")
    notes.add_note("meeting notes")
    result = notes.find_text_in_note("milk")
    assert result == ["shopping list: milk"]