# Bots Team CLI Assistant

**Bots Team** is a command-line assistant bot written in Python. It allows you to manage contacts and notes using structured commands and persistent storage.

## Features

* Contact management: phones, emails, addresses, birthdays
* Notes with tags
* Search by name, email, or address
* View upcoming birthdays
* Persistent storage using pickle
* Command suggestions for mistyped input
* Interactive CLI interface via `prompt_toolkit`

## Installation

### Option 1: Run directly (development mode)

```bash
cd src
python -m bots_team.main
```

### Option 2: Install as a CLI tool

```bash
pip install -e .
bots
```

## Project Structure

```
.
├── pyproject.toml
├── requirements.txt
└── src/
    └── bots_team/
        ├── main.py
        ├── models/
        ├── handlers/
        └── data/
```

## Requirements

* Python 3.8+
* prompt\_toolkit

##
for tests ```PYTHONPATH=src python3 -m pytest```