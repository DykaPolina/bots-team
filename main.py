"""
Entry point for the assistant bot.
Handles command parsing and control loop.
"""

from src.models.storage import load_data
from src.handlers.utils import parse_input, suggest_command
from src.handlers.handlers import command_hindler, get_available_commands
from src.models.classNotes import Notes


def main():
    book = load_data()
    notes = Notes()
    available_commands = get_available_commands()
    
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue  
            
        command, args = parse_input(user_input)

        if command in available_commands:
            try:
                result = command_hindler(command, book, args, notes)
                if result is None:
                    break
                print(result)
            except SystemExit as e:
                print(e)
                break
        else:
            suggested = suggest_command(command, available_commands)
            if suggested:
                print(f"Команда '{command}' не розпізнана. Можливо, ви мали на увазі: '{suggested}'? (y/n)")
                confirmation = input().strip().lower()
                if confirmation == "y":
                    result = command_hindler(suggested, book, args, notes)
                    if result is None:
                        break
                    print(result)
                else:
                    print("Спробуйте іншу команду.")
            else:
                print("Невідома команда. Введіть 'help' для списку.")


if __name__ == "__main__":
    main()