import models
from connection import db
from datetime import datetime
from process import note_printer

db.connect()
db.drop_tables([models.Notes])
db.create_tables([models.Notes])

notes = [{
    'title': "New Note",
    'contents': 'This is an important message',
    'timestamp': datetime.now(),
    'username': 'psql'
},{
    'title': "rm reminder",
    'contents': 'DON\'T USE rm -rf EVER',
    'timestamp': datetime.now(),
    'username': 'Ethan'
},{
    'title': 'How does css work?',
    'contents': 'box-sizing: border-box;',
    'timestamp': datetime.now(),
    'username': 'psql'
},{
    'title': "Grocery List",
    'contents': 'Eggs, Milk, Bread, Yogurt',
    'timestamp': datetime.now(),
    'username': 'Ethan'
},{
    'title': "Databases are rad",
    'contents': '😀😃😄😁😆😅😂🤣☺️😇🙂🙃😉😍😘😗😙😋😛😝😜🤪🤨🧐🤓😎🤩😏😒😞😔😟😕🙁☹️😣😖',
    'timestamp': datetime.now(),
    'username': 'psql'
},{
    'title': "...",
    'contents': 'uhhh, running out of ideas',
    'timestamp': datetime.now(),
    'username': 'Ethan'
},{
    'title': "Make a README!",
    'contents': 'Don\'t forget to make your README.md! It\'s this most important part!',
    'timestamp': datetime.now(),
    'username': 'psql'
}]

for note in notes:
    new_note = models.Notes(**note)
    new_note.save()
    note_printer(new_note)
