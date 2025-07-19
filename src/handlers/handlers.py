"""
Handlers for each bot command.
"""

from .utils import input_error, execute_command
from src.models.classNotes import Notes
from src.models.address_book import AddressBook
from src.models.storage import save_data

from src.handlers.handlers_contact import add_contact, change_contact, show_phone, show_all, remove_phone, find_phone, delete_contact
from src.handlers.handlers_address import set_address, show_address, remove_address
from src.handlers.handlers_email import add_email, change_email, show_email, remove_email, find_email
from src.handlers.handlers_birthday import set_birthday, show_birthday, remove_birthday, birthdays
from src.handlers.handlers_note import command_add_note, command_delete_note, command_edit_note, command_find_all_note, command_find_text_in_note
from src.handlers.handlers_tags import command_add_tag, command_delete_tags, command_show_all_tags

def command_hello():
    return "How can I help you?"

def help_command(args):
    """
    Show available commands and usage.
    Usage: help
    """
    if args:
        return "Usage: help"
    return (
        "Available commands:\n"
        "  hello                         - Greet the bot\n"
        "  add [name] [phones...]        - Add contact with one or more phone numbers\n"
        "  change [name] [old] [new]     - Replace old phone with new\n"
        "  phone [name]                  - Show contact's phones\n"
        "  all                           - Show all contacts\n"
        "  set-birthday [name] [date]    - Set birthday in DD.MM.YYYY format\n"
        "  show-birthday [name]          - Show birthday of contact\n"
        "  birthdays [days]              - Show upcoming birthdays in the given number of days\n"
        "  remove-phone [name] [phone]   - Remove a phone number\n"
        "  find-phone [name] [phone]     - Check if phone exists\n"
        "  delete-contact [name]         - Remove the entire contact\n"
        "  help                          - Show this help message\n"
        "  close / exit                  - Exit the program"
    )

def command_exit(book: AddressBook):
    save_data(book)
    raise SystemExit("Good bye!")

@input_error
def command_hindler(command, book, args, notes):
    command_list = {
        "hello": command_hello,

        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,

        "set-adress": set_address,
        "show-address": show_address,
        "remove_address": remove_address,

        "add-email": add_email,
        "change_email": change_email,
        "show_email": show_email,
        "remove_email": remove_email,
        "find_email": find_email,

        "set-birthday": set_birthday,
        "show-birthday": show_birthday,
        "remove_birthday": remove_birthday,
        "birthdays": birthdays,

        "remove-phone": remove_phone,
        "find-phone": find_phone,
        "delete-contact": delete_contact,

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

    }

    return execute_command(command_list[command], {"book": book, "args": args, "notes": notes})
    