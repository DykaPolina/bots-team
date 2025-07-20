from bots_team.models.notes import Notes

def note_format(args):
        return " ".join(args)


def command_add_note(args, notes: Notes):
    if not args:
        return "Usage: add-note [text] or add-note [text]; [tag1 tag2 ...]"

    text = " ".join(args)
    if ";" in text:
        note, tags_str = text.split(";", 1)
        note = note.strip()
        tags = tags_str.strip().split()
    else:
        note = text.strip()
        tags = []

    result = notes.add_note(note)
    if tags:
        instance_note = notes.find_note(note)
        result_tags = instance_note.add_tags(tags)
        return f"{result}\n{result_tags}"

    return result


def command_edit_note(args, notes: Notes):
    if not args or ";" not in note_format(args):
        return "Usage: edit-note [old]; [new]"
    note, new_note = note_format(args).split(";", 1)
    return notes.edit_note(note, new_note.lstrip())


def command_find_all_note(notes: Notes, args=None):
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

