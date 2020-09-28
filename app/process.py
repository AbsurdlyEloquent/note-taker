# DEPENDECIES
import sys
import os
from datetime import datetime
from dependencies.colors import *

# MODULE IMPORTS
from db.models import Notes

# FUNCTIONS
def list_commands(user):
    print("""
Here's a list of commands:
    help: Shows a list of commands (you're here now)
    exit: Exits the app
    new: Creates a new note
    get: Displays one note by its id
    ls: Lists all the notes you've created
    ls -a: Lists all the notes ever created
    update: Updates a note by its id
    rm: Removes a note by its id
           """)

def exit(sig, frame=None):
    with pretty_output(BOLD, FG_MAGENTA) as out:
        out.write('\nGoodbye!\n')
    sys.exit(0)

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
    note_printer(new_note)

def list(user):
    os.system('clear')
    with pretty_output(BOLD) as out:
        out.write(f'Here are all the notes written by {user}:')
    for note in Notes.select().where(Notes.username == user):
        note_printer(note)

def list_all(user):
    os.system('clear')
    query = Notes.select()
    with pretty_output(BOLD) as out:
        out.write('Here are all the notes in this system:')
    for note in query:
        note_printer(note)

def get_one(user):
    os.system('clear')
    query = Notes.get_by_id(input('Enter the ID of the note to get: '))
    with pretty_output(BOLD, FG_BLUE) as out:
        out.write('Here is the requested note:')
    note_printer(query)

def update_note(user):
    os.system('clear')
    note_id = input('Enter the ID of the note to update: ')
    note = Notes.get_by_id(note_id)
    new_title = input(f'Enter a new title: (to skip press enter)\n{note.title} >> ')
    if len(new_title) > 0:
        query = Notes.update(title=new_title).where(Notes.id == note_id)
        query.execute()
    new_contents = input('Enter a new note: (to skip press enter)\n>> ')
    if len(new_contents) > 0:
        query = Notes.update(contents=new_contents).where(Notes.id == note_id)
        query.execute()
    query = Notes.update(timestamp=datetime.now(), username=user).where(Notes.id == note_id)
    query.execute()
    updated_note = Notes.get_by_id(note_id)
    with pretty_output(BOLD, FG_GREEN) as out:
        out.write('Success!', ' ')
    print('Here is your updated note:')
    note_printer(updated_note)

def delete_note(user):
    os.system('clear')
    note_id = input('Enter the ID of the note to delete: ')
    note = Notes.get_by_id(note_id)
    note_printer(note)
    with pretty_output(BOLD) as out:
        out.write('Are you sure you want to delete this?', " ")
    with pretty_output(BOLD, FG_RED) as out:
        out.write("This action cannot be undone", " ")
    while True:
        res = input("(y/n): ")
        if res == 'y':
            note.delete_instance()
            with pretty_output(FG_GREEN) as out:
                out.write('Successfully removed note...')
            break
        elif res == 'n':
            break
        else:
            pass

def note_printer(note):
    with pretty_output(BOLD, FG_CYAN) as out:
        out.write(note.title, " ")
    with pretty_output(BOLD, FG_MAGENTA) as out:
        out.write(f'ID: {note.id}')
    with pretty_output(FG_BLUE) as out:
        out.write(f"by {note.username} on {note.timestamp}")
    with pretty_output(BOLD) as out:
        out.write(note.contents, '\n\n')

def error(user):
    with pretty_output(BOLD, FG_RED) as out:
        out.write('Error!', ' ')
    with pretty_output(BOLD) as out:
        out.write('Command not found, enter help for a list of commands')
