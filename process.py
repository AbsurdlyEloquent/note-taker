# DEPENDECIES
import sys
import os
from datetime import datetime
from dependencies.colors import *

# MODULE IMPORTS
from db.models import Notes

# FUNCTIONS
def list_commands(user):
    print("""Here's a list of commands:\n
           help: Shows a list of commands (you're here now)\n
           new: Creates a new note""")

def exit(user):
    with pretty_output(BOLD, FG_MAGENTA) as out:
        out.write('Goodbye!\n')
    sys.exit()

def create_note(user):
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
        out.write(note['title'])
    with pretty_output(DIM, FG_CYAN) as out:
        out.write(f"by {note['username']} on {note['timestamp']}")
    with pretty_output(BOLD) as out:
        out.write(note['contents'], '\n\n')
