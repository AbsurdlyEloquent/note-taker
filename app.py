
# DEPENDECIES
import os
import process

# GLOBAL VARI'S
user = None

# COMMANDS
def commands(command):
    switcher = {
        'help': process.list_commands,
        'exit': process.exit,
        'new': process.create_note,
        'ls': process.list,
        'ls -a': process.list_all
    }
    func = switcher[command]
    if func:
        return func
    else:
        return process.error

# WORKFLOW START
os.system('clear')
if not user:
    user = input('Enter your name: ')
    print('Welcome to Note Taker!! :) Enter help for a list of commands')
while True:
    command_prompt = input('Note Taker >> ')
    commands(command_prompt)(user)
