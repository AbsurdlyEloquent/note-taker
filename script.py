"""
Peewee models
"""
import datetime
import peewee

db = peewee.PostgresqlDatabase('notes', user='person', password='1234',
                                    host='localhost', port=5432)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class User(BaseModel):
    username = peewee.CharField(max_length=20)

class Note(BaseModel):
    title = peewee.CharField(max_length=20)
    note = peewee.CharField()
    timestamp = peewee.DateTimeField(deault=datetime.datetime.now)

db.connect()
db.drop_tables([User, Note])
db.create_tables([User, Note])
