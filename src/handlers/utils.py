"""
Utility functions for input handling and decorators.
"""

def input_error(func):
    """
    Decorator to handle common input errors and return user-friendly messages.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Enter the argument for the command."
        except Exception as e:
            print(f"{e}")
    return inner

def parse_input(user_input):
    """
    Parse user input into a command and a list of arguments.

    Returns:
        tuple[str, list[str]]: The command and its arguments
    """
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args
