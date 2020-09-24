import datetime
from connection import db
import peewee as p

class BaseModel(p.Model):
    class Meta:
        database = db

class User(BaseModel):
    username = p.CharField(max_length=20)

class Note(BaseModel):
    title = p.CharField(max_length=20)
    note = p.CharField()
    timestamp = p.DateTimeField(default=datetime.datetime.now)
    user = p.ForeignKeyField(User, backref='notes')
