"""
Entry point for the assistant bot.
Handles command parsing and control loop.
"""

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import print_formatted_text

from src.models.storage import load_data, load_notes
from src.handlers.utils import parse_input, suggest_command
from src.handlers.handlers import command_handler, get_available_commands


def print_colored(text):
    print_formatted_text(HTML(text))


def main():
    book = load_data()
    notes = load_notes()
    available_commands = get_available_commands()
    completer = WordCompleter(available_commands, ignore_case=True)
    session = PromptSession(completer=completer)

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
            try:
                result = command_handler(command, book, args, notes)
                if result is None:
                    break
                print_colored(f"<lightgreen>{result}</lightgreen>")
            except SystemExit as e:
                print_colored(f"<purple>{e}</purple>")
                break
        else:
            suggested = suggest_command(command, available_commands)
            if suggested:
                confirm = session.prompt(
                    HTML(f"<ansiyellow>Команда '{command}' не розпізнана. Можливо, ви мали на увазі: '<b>{suggested}</b>'? (y/n)</ansiyellow> ")
                ).strip().lower()
                if confirm == 'y':
                    result = command_handler(suggested, book, args, notes)
                    if result is None:
                        break
                    print_colored(f"<lightgreen>{result}</lightgreen>")
                else:
                    print_colored("<ansiyellow>Спробуйте іншу команду.</ansiyellow>")
            else:
                print_colored("<ansired>Невідома команда. Введіть 'help' для списку.</ansired>")


if __name__ == "__main__":
    main()
