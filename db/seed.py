import models
from connection import db

db.connect()
db.drop_tables([models.User, models.Note])
db.create_tables([models.User, models.Note])

admin = models.User(username='admin')
admin.save()

user = models.User.get(models.User.username == 'admin')
print(user.username)
