from db.connection import db
from db.models import User, Note

login_prompt = input('Do you want to login or create a user?\n')

if login_prompt == 'login':
    login()
else:
    create_user()

def login():
    username = input('Enter username:')
    user = User.get(User.username == username)
    print(user)
