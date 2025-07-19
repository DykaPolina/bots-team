from src.models.classNotes import Notes
def note_format(args):
        return " ".join(args)


def command_add_note(args, notes: Notes):
    note = note_format(args)
    return notes.add_note(note)


def command_edit_note(args, notes: Notes):
    note, new_note = note_format(args).split(";")
    return notes.edit_note(note, new_note.lstrip())


def command_find_all_note(notes: Notes):
    return notes.find_all_note()


def command_delete_note(args, notes: Notes):
    note = note_format(args)
    return notes.delete_note(note)


def command_find_text_in_note(args, notes: Notes):
    text = note_format(args)
    return notes.find_text_in_note(text)

