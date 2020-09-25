# DEPENDECIES
from datetime import datetime

# MODULE IMPORTS
from db.connection import db
from db.models import Users, Notes
from process import *

# GLOBAL VARIABLES
user = None
note = None

# PROCESS FUNCTIONS
def list_commands():
    print("Here's a list of commands:\n
           help: Shows a list of commands (you're here now)\n
           login: Lets you log in or create a new user\n
           new note: Creates a new note")

def login(username=None):
    if not username:
        create_prompt = input('Do you have an account? (y/n) ')
        if create_prompt == 'y':
            username = input('Enter username:')
        else: create_user()
    global user
    user = Users.get(Users.username == user.username)
    print(f'logged in as {user.username}')

def create_user():
    username = input('Enter a username:')
    global user
    user = Users(username=username)
    user.save()
    login(user.username)

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
        'help': list_commands(),
        'login': login(),
        'new note': create_note(),
    }
    func = switcher.get(command, lambda: "Command not found, enter help for a list of commands")
    func()

command_prompt = input('Note Taker >> ')
while True:
    commands(command_prompt)
