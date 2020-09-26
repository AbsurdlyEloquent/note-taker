# DEPENDECIES
from datetime import datetime

# MODULE IMPORTS
from db.connection import db
from db.models import Notes
from process import *

# GLOBAL VARIABLES
user = None
note = None

# PROCESS FUNCTIONS
def list_commands():
    print("""Here's a list of commands:\n
           help: Shows a list of commands (you're here now)\n
           login: Lets you log in or create a new user\n
           new note: Creates a new note""")

def create_note():
    global note
    note = {
        "title": input("Enter a title for your note: (20 Char limit)\n"),
        "contents": input("Enter your note: (255 Char limit)\n"),
        "timestamp": datetime.now(),
        "user": user
    }

# COMMANDS
def commands(command):
    switcher = {
        'help': list_commands,
        'note': create_note
    }
    return switcher[command]

while True:
    command_prompt = input('Note Taker >> ')
    commands(command_prompt)()
