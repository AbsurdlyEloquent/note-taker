import sys
import os
# DEPENDECIES
from datetime import datetime
from dependencies.colors import *

# MODULE IMPORTS
from db.connection import db
from db.models import Notes

# GLOBAL VARIABLES
user = None

# PROCESS FUNCTIONS
def list_commands():
    print("""Here's a list of commands:\n
           help: Shows a list of commands (you're here now)\n
           note: Creates a new note""")

def exit():
    with pretty_output(BOLD, BG_MAGENTA) as out:
        out.write('Goodbye!\n')
    sys.exit()

def create_note():
    os.system('clear')
    note = {
        "title": input("Enter a title for your note: (20 Char limit)\n"),
        "contents": input("Enter your note: (255 Char limit)\n"),
        "timestamp": datetime.now(),
        "username": user
    }
    Notes.create(**note)
    with pretty_output(BOLD, FG_GREEN) as out:
        out.write('Success!', ' ')
    print('Here is your new note:')
    with pretty_output(BOLD, FG_CYAN) as out:
        out.write(note['title'], ' ')
    with pretty_output(DIM) as out:
        out.write(f"{note['timestamp']}")
    with pretty_output(DIM) as out:
        out.write(f"by {note['username']}")
    with pretty_output(BOLD) as out:
        out.write(note['contents'], '\n\n')


# COMMANDS
def commands(command):
    switcher = {
        'help': list_commands,
        'exit': exit,
        'note': create_note,

    }
    return switcher[command]

# WORKFLOW START
os.system('clear')
if not user:
    user = input('Enter your name: ')
    print('Welcome to Note Taker!! :) Enter help for a list of commands')
while True:
    command_prompt = input('Note Taker >> ')
    commands(command_prompt)()
