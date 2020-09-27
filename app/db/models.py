import datetime
from db.connection import db
import peewee as p

class BaseModel(p.Model):
    class Meta:
        database = db

class Notes(BaseModel):
    title = p.CharField(max_length=20)
    contents = p.CharField()
    timestamp = p.DateTimeField(default=datetime.datetime.now)
    username = p.CharField(max_length=20)
