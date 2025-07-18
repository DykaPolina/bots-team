import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.handlers.utils import parse_input, suggest_command, input_error, execute_command



def test_parse_input():
    user_input = "add Polina 0501234567"
    command, args = parse_input(user_input)
    assert command == "add"
    assert args == ["Polina", "0501234567"]


def test_suggest_command_found():
    available = ["add", "edit", "delete", "exit"]
    suggestion = suggest_command("adde", available)
    assert suggestion == "add"

def test_suggest_command_not_found():
    available = ["add", "edit", "delete", "exit"]
    suggestion = suggest_command("qwerty", available)
    assert suggestion is None


@input_error
def error_func_key():
    raise KeyError("test")

@input_error
def error_func_value():
    raise ValueError("invalid")

@input_error
def error_func_index():
    raise IndexError()

@input_error
def error_func_other():
    raise RuntimeError("boom")


def test_input_error_decorator():
    assert error_func_key() == "Enter user name."
    assert error_func_value() == "invalid"
    assert error_func_index() == "Enter the argument for the command."
    assert error_func_other() == "Unexpected error: RuntimeError: boom"


def dummy_func(name, age=18):
    return f"{name} is {age}"

def test_execute_command_with_required_only():
    result = execute_command(dummy_func, {"name": "Polina"})
    assert result == "Polina is 18"

def test_execute_command_with_all_args():
    result = execute_command(dummy_func, {"name": "Pasha", "age": 30})
    assert result == "Pasha is 30"

def test_execute_command_missing_param():
    with pytest.raises(ValueError, match="Missing required parameter: name"):
        execute_command(dummy_func, {})
