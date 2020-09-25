import datetime
from db.connection import db
import peewee as p

class BaseModel(p.Model):
    class Meta:
        database = db

class Users(BaseModel):
    username = p.CharField(max_length=20)

class Notes(BaseModel):
    title = p.CharField(max_length=20)
    contents = p.CharField()
    timestamp = p.DateTimeField(default=datetime.datetime.now)
    user = p.ForeignKeyField(Users, backref='notes')
