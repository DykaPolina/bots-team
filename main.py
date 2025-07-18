"""
Entry point for the assistant bot.
Handles command parsing and control loop.
"""
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import print_formatted_text

import difflib
from prompt_toolkit import prompt
from src.models.storage import load_data, save_data
from src.handlers.utils import parse_input
from src.handlers.handlers import (
    add_contact, change_contact, show_phone, show_all,
    set_address, show_address, remove_address, add_email,
    change_email, show_email, remove_email, find_email,
    set_birthday, show_birthday, remove_birthday, birthdays,
    remove_phone, find_phone, delete_contact, search, help_command
)

"""може ці дві наступні функції винести з мєйн файлу?"""
def suggest_command(user_input, available_commands):
    close_matches = difflib.get_close_matches(user_input, available_commands, n=1, cutoff=0.6)
    if close_matches:
        return close_matches[0]
    else:
        return None

def execute_command(command, args, book):   
    match command:
        case "close" | "exit":
            save_data(book)
            print_colored("<purple>Good bye!</purple>")
            return False
        case "hello":
            print_colored("<lightgreen>How can I help you?</lightgreen>")
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
        case "search":
            print(search(args, book))
        case "help":
            print(help_command(args, book))
        case "search":
            print(search(args, book))
        case _:
            print("Invalid command.")
    return True

def print_colored(text):
    print_formatted_text(HTML(text))

def main():
    available_commands = [
        "add", "change", "phone", "all", "help", "close", "exit", "hello",
        "add-address", "show-address", "remove-address",
        "add-email", "change-email", "show-email", "remove-email", "find-email",
        "set-birthday", "show-birthday", "remove-birthday", "birthdays",
        "remove-phone", "find-phone", "delete-contact", "search"
    ]
    completer = WordCompleter(available_commands, ignore_case=True)
    session = PromptSession(completer=completer)
    
    """Run the command-line assistant bot."""
    book = load_data()
    print_colored("<green>Welcome to the assistant bot!</green>")
    
    while True:
        try:
            user_input = session.prompt(HTML('<skyblue>Enter a command:</skyblue> ')).strip()
        except KeyboardInterrupt:
            continue
        except EOFError:
            print_colored("<green>Good bye!</green>")
            break

        if not user_input:
            continue  

        parsed = parse_input(user_input)
        if not parsed:
            print_colored("<ansiyellow>Не вдалося розпізнати команду. Введіть 'help' для списку.</ansiyellow>")
            continue          

        command, args = parsed

       
        if command in available_commands:
            if not execute_command(command, args, book):
                break
        else:
            suggested = suggest_command(command, available_commands)
            if suggested:
                confirm = session.prompt(
                    HTML(f"<ansiyellow>Команда '{command}' не розпізнана. Можливо, ви мали на увазі: '<b>{suggested}</b>'? (y/n)</ansiyellow> ")
                ).strip().lower()
                if confirm == 'y':
                    if not execute_command(suggested, args, book):
                        break
                else:
                    print_colored("<ansiyellow>Cпробуйте іншу команду.</ansiyellow>")
            else:
                print_colored("<ansired>Невідома команда. Введіть 'help' для списку.</ansired>")



if __name__ == "__main__":
    main()
