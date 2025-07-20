"""
Handlers for each bot command.
"""

from .utils import input_error, execute_command
from bots_team.models.notes import Notes
from bots_team.models.address_book import AddressBook
from bots_team.models.storage import save_data, save_notes

from bots_team.handlers.handlers_contact import add_contact, change_contact, show_phone, show_all, remove_phone, find_phone, delete_contact, search
from bots_team.handlers.handlers_address import set_address, show_address, remove_address
from bots_team.handlers.handlers_email import add_email, change_email, show_email, remove_email, find_email
from bots_team.handlers.handlers_birthday import set_birthday, show_birthday, remove_birthday, birthdays
from bots_team.handlers.handlers_note import command_add_note, command_delete_note, command_edit_note, command_find_all_note, command_find_text_in_note
from bots_team.handlers.handlers_tags import command_add_tag, command_delete_tags, command_show_all_tags, command_find_notes_by_tag

def get_available_commands():
    return list(command_list.keys())

def command_hello():
    return "How can I help you?"

def help_command(args=None):
    """
    Show available commands and usage.
    Usage: help
    """
    if args:
        return "Usage: help"
    return (
        "Available commands:\n"
        "  hello                          - Greet the bot\n"
        "  add [name] [phones...]         - Add contact with one or more phone numbers\n"
        "  change [name] [old] [new]      - Replace old phone with new\n"
        "  phone [name]                   - Show contact's phone numbers\n"
        "  all                            - Show all contacts\n"
        "  delete-contact [name]          - Remove the entire contact\n"
        "  search [query]                 - Search contacts by name, email, or address\n"
        "\n"
        "Address:\n"
        "  set-address [name] [address]   - Set or update address\n"
        "  show-address [name]            - Show contact's address\n"
        "  remove-address [name]          - Remove contact's address\n"
        "\n"
        "Email:\n"
        "  add-email [name] [email]       - Add email to contact\n"
        "  change-email [name] [old] [new]- Change email\n"
        "  show-email [name]              - Show all emails\n"
        "  remove-email [name] [email]    - Remove specific email\n"
        "  find-email [name] [email]      - Find specific email\n"
        "\n"
        "Birthday:\n"
        "  set-birthday [name] [DD.MM.YYYY] - Set birthday\n"
        "  show-birthday [name]           - Show birthday\n"
        "  remove-birthday [name]         - Remove birthday\n"
        "  birthdays [days]               - Show upcoming birthdays within days\n"
        "\n"
        "Phone (additional):\n"
        "  remove-phone [name] [phone]    - Remove specific phone number\n"
        "  find-phone [name] [phone]      - Find specific phone number\n"
        "\n"
        "Notes:\n"
        "  add-note [text]                - Add a note\n"
        "  edit-note [old]; [new]         - Edit a note (separate old and new by semicolon)\n"
        "  delete-note [text]             - Delete a note\n"
        "  find-all-note                  - Show all notes\n"
        "  find-text-in-note [text]       - Find notes containing text\n"
        "Tags:\n"
        "  add-tags [note]; [tag1 tag2]   - Add tags to a note\n"
        "  delete-tags [note]; [tag1 tag2]- Remove tags from a note\n"
        "  all-tags [note]                - Show all tags of a note\n"
        "  find-by-tag [tag]                - Find all notes with a specific tag\n"
        "\n"
        "System:\n"
        "  help                           - Show this help message\n"
        "  close / exit                   - Exit the assistant\n"
    )

def command_exit(book: AddressBook, notes: Notes):
    save_data(book)
    save_notes(notes)
    raise SystemExit("Good bye!")

    
command_list = {
        "hello": command_hello,

        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,

        "set-address": set_address,
        "show-address": show_address,
        "remove-address": remove_address,

        "add-email": add_email,
        "change-email": change_email,
        "show-email": show_email,
        "remove-email": remove_email,
        "find-email": find_email,

        "set-birthday": set_birthday,
        "show-birthday": show_birthday,
        "remove-birthday": remove_birthday,
        "birthdays": birthdays,

        "remove-phone": remove_phone,
        "find-phone": find_phone,
        "delete-contact": delete_contact,

        "search": search,

        "help": help_command,
        "exit": command_exit,
        "close": command_exit,

        "add-note": command_add_note,
        "edit-note": command_edit_note,
        "find-all-note": command_find_all_note,
        "delete-note": command_delete_note,
        "find-text-in-note": command_find_text_in_note,

        "add-tags": command_add_tag,
        "delete-tags": command_delete_tags,
        "all-tags": command_show_all_tags,
        "find-by-tag": command_find_notes_by_tag,

    }


@input_error
def command_handler(command, book, args, notes):
    return execute_command(command_list[command], {"book": book, "args": args, "notes": notes})
    