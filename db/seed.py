import models
from connection import db

db.connect()
db.drop_tables([models.Users, models.Notes])
db.create_tables([models.Users, models.Notes])

admin = models.Users(username='admin')
admin.save()

user = models.Users.get(models.Users.username == 'admin')
print(user.username)
