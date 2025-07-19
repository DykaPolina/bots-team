from src.models.classNotes import Notes
from src.handlers.handlers_note import note_format

def command_add_tag(args, notes: Notes):
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

