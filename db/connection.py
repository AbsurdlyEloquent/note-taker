import peewee as p

db = p.PostgresqlDatabase('notes', user='person', password='1234',
                                    host='localhost', port=5432)
