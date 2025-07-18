"""
Entry point for the assistant bot.
Handles command parsing and control loop.
"""

from src.models.storage import load_data
from src.handlers.utils import parse_input
from src.handlers.handlers import command_hindler
from src.models.classNotes import Notes

def main():
    """Run the command-line assistant bot."""
    book = load_data()
    print("Welcome to the assistant bot!")
    notes = Notes()

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
        command, args = parse_input(user_input)
        print(command_hindler(command, book, args, notes))

if __name__ == "__main__":
    main()
