from src.models.notes import Notes

def note_format(args):
        return " ".join(args)


def command_add_note(args, notes: Notes):
    if not args:
        return "Usage: add-note [text]"
    note = note_format(args)
    return notes.add_note(note)


def command_edit_note(args, notes: Notes):
    if not args or ";" not in note_format(args):
        return "Usage: edit-note [old]; [new]"
    note, new_note = note_format(args).split(";", 1)
    return notes.edit_note(note, new_note.lstrip())


def command_find_all_note(notes: Notes):
    return notes.find_all_note()


def command_delete_note(args, notes: Notes):
    if not args:
        return "Usage: delete-note [text]"
    note = note_format(args)
    return notes.delete_note(note)


def command_find_text_in_note(args, notes: Notes):
    if not args:
        return "Usage: find-text-in-note [text]"
    text = note_format(args)
    return notes.find_text_in_note(text)

