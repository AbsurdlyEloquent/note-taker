# DEPENDECIES
import sys
import os
from datetime import datetime
from dependencies.colors import *

# MODULE IMPORTS
from db.models import Notes

# FUNCTIONS
def list_commands(user):
    print("""Here's a list of commands:
           help: Shows a list of commands (you're here now)
           exit: Exits the app
           new: Creates a new note
           ls: Lists all the notes you've created
           ls -a: Lists all the notes ever created""")

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
    new_note = Notes.create(**note)
    with pretty_output(BOLD, FG_GREEN) as out:
        out.write('Success!', ' ')
    print('Here is your new note:')
    note_printer(**new_note)

def list(user):
    os.system('clear')
    with pretty_output(BOLD) as out:
        out.write(f'Here are all the notes written by {user}')
    for note in Notes.select().where(Notes.username == user):
        note_printer(note)

def list_all(user):
    os.system('clear')
    query = Notes.select()
    with pretty_output(BOLD) as out:
        out.write('Here are all the notes in this system:')
    for note in query:
        note_printer(note)



def note_printer(note):
    with pretty_output(BOLD, FG_CYAN) as out:
        out.write(note.title, " ")
    with pretty_output(BOLD, FG_MAGENTA) as out:
        out.write(f'ID: {str(note.id)}')
    with pretty_output(FG_BLUE) as out:
        out.write(f"by {note.username} on {note.timestamp}")
    with pretty_output(BOLD) as out:
        out.write(note.contents, '\n\n')

def error(user):
    with pretty_output(BOLD, FG_RED) as out:
        out.write('Error!', ' ')
    with pretty_output(BOLD) as out:
        out.write('Command not found, enter help for a list of commands')
