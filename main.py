"""
Entry point for the assistant bot.
Handles command parsing and control loop.
"""

from src.models.storage import load_data, save_data
from src.handlers.utils import parse_input
from src.handlers.handlers import (
    add_contact, change_contact, show_phone, show_all,
    set_address, show_address, remove_address, add_email,
    change_email, show_email, remove_email, find_email,
    set_birthday, show_birthday, remove_birthday, birthdays,
    remove_phone, find_phone, delete_contact, help_command
)

def main():
    """Run the command-line assistant bot."""
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                save_data(book)
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(show_phone(args, book))
            case "all":
                print(show_all(book))
            case "add-address":
                print(set_address(args, book))
            case "show-address":
                print(show_address(args, book))
            case "remove-address":
                print(remove_address(args, book))
            case "add-email":
                print(add_email(args, book))
            case "change-email":
                print(change_email(args, book))
            case "show-email":
                print(show_email(args, book))
            case "remove-email":
                print(remove_email(args, book))
            case "find-email":
                print(find_email(args, book))
            case "set-birthday":
                print(set_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "remove-birthday":
                print(remove_birthday(args, book))
            case "birthdays":
                print(birthdays(args, book))
            case "remove-phone":
                print(remove_phone(args, book))
            case "find-phone":
                print(find_phone(args, book))
            case "delete-contact":
                print(delete_contact(args, book))
            case "help":
                print(help_command(args, book))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
