import peewee as p

db = p.PostgresqlDatabase('notes', user='psql', password='',
                                    host='localhost', port=5432)
