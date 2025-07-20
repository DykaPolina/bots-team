"""
Utility functions for input handling and decorators.
"""

import inspect
import functools
import difflib


def suggest_command(user_input, available_commands):
    close_matches = difflib.get_close_matches(user_input, available_commands, n=1, cutoff=0.6)
    return close_matches[0] if close_matches else None

def input_error(func):
    """
    Decorator to handle common input errors and return user-friendly messages.
    """
    @functools.wraps(func)
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
            return f"Unexpected error: {type(e).__name__}: {e}"
    return inner

def parse_input(user_input):
    """
    Parse user input into a command and a list of arguments.

    Returns:
        tuple[str, list[str]]: The command and its arguments
    """
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

def execute_command(func, args_dict: dict):
 
    sig = inspect.signature(func)
    bound_args = {} 
    for param in sig.parameters.values():
        if param.name in args_dict:
            bound_args[param.name] = args_dict[param.name]
        elif param.default is not param.empty:
            bound_args[param.name] = param.default
        else:
            raise ValueError(f"Missing required parameter: {param.name}")

    return func(**bound_args)