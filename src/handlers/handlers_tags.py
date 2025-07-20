from src.models.notes import Notes
from src.handlers.handlers_note import note_format

def command_add_tag(args, notes: Notes):
    if ";" not in note_format(args):
      return "Usage: add-tags [note]; [tag1 tag2]"
    note, tags = note_format(args).split(";")
    instance_note = notes.find_note(note)
    return instance_note.add_tags(tags.split())


def command_delete_tags(args, notes: Notes):
    note, tags = note_format(args).split(";")
    instance_note = notes.find_note(note)
    return instance_note.delete_tag(tags.split())


def command_show_all_tags(args, notes: Notes):
    note = note_format(args)
    instance_note = notes.find_note(note)
    return instance_note.show_all_tag()

def command_find_notes_by_tag(args, notes: Notes):
    if not args:
        return "Usage: find-by-tag [tag]"
    tag = args[0]
    result = notes.find_notes_by_tag(tag)
    return "\n".join(result) if result else "No notes found with that tag."

