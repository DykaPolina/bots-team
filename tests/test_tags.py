import pytest
from src.bots_team.models.notes import Notes
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_add_tags_success():
    notes = Notes()
    notes.add_note("Buy milk")
    result = notes.find_note("Buy milk").add_tags(["food", "shopping"])
    assert "tags added successfully" in result
    assert set(notes.find_note("Buy milk").show_all_tag()) == {"food", "shopping"}


def test_add_existing_tag_raises_exception():
    notes = Notes()
    notes.add_note("Buy milk")
    notes.find_note("Buy milk").add_tags(["food"])
    with pytest.raises(Exception) as exc:
        notes.find_note("Buy milk").add_tags(["food"])
    assert "Tag already exist" in str(exc.value)


def test_delete_tags_success():
    notes = Notes()
    notes.add_note("Do homework")
    notes.find_note("Do homework").add_tags(["school", "math"])
    result = notes.find_note("Do homework").delete_tag(["school"])
    assert "tags deleted successfully" in result
    assert notes.find_note("Do homework").show_all_tag() == ["math"]


def test_delete_nonexistent_tag_raises_exception():
    notes = Notes()
    notes.add_note("Walk dog")
    notes.find_note("Walk dog").add_tags(["pets"])
    with pytest.raises(Exception):
        notes.find_note("Walk dog").delete_tag(["work"])


def test_show_all_tags():
    notes = Notes()
    notes.add_note("Read book")
    notes.find_note("Read book").add_tags(["leisure", "hobby"])
    tags = notes.find_note("Read book").show_all_tag()
    assert set(tags) == {"leisure", "hobby"}


def test_find_notes_by_tag():
    notes = Notes()
    notes.add_note("Note 1")
    notes.add_note("Note 2")
    notes.add_note("Note 3")
    notes.find_note("Note 1").add_tags(["work"])
    notes.find_note("Note 2").add_tags(["work", "urgent"])
    notes.find_note("Note 3").add_tags(["personal"])

    result = notes.find_notes_by_tag("work")
    assert set(result) == {"Note 1", "Note 2"}

    result = notes.find_notes_by_tag("personal")
    assert result == ["Note 3"]

    result = notes.find_notes_by_tag("nonexistent")
    assert result == []
