# DEPENDECIES
from datetime import datetime

# MODULE IMPORTS
from db.connection import db
from db.models import User, Note

# GLOBAL VARIABLES
user = None
note = None

# PROCESS FUNCTIONS
def login(username=None):
    if not username:
        username = input('Enter username:')
    global user
    user = User.get(User.username == username)
    print(f'logged in as {user.username}')

def create_user():
    username = input('Enter a username:')
    global user
    user = User(username=username)
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

## BEGINNING OF WORKFLOW
while not user:
    login_prompt = input('Do you want to login or create a user?\n')
    if login_prompt == 'login':
        login()
    elif login_prompt == 'create':
        create_user()

new_note = input('Would you like to write a note? (y/n)')
if new_note == 'y':
    create_note()
    print(f'{note["title"]}\n{note["contents"]}')
    submit_note = input('Is this correct? (y/n)')
    if submit_note == 'y':
        submitted_note = Note(**note)
        submitted_note.save()
query = Note.select().join(User).where(User.id == user.id)
for note in query:
    print(f'{note.title} {note.timestamp}\n{note.user.username}\n{note.contents}\n')
