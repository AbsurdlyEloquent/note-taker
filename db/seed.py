import models
from connection import db

db.connect()
db.drop_tables([models.Notes])
db.create_tables([models.Notes])
