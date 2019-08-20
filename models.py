from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('tasks.sqlite')


class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    login = DateTimeField()
    logout = DateTimeField()
    user = IntegerField()

    class Meta:
        # //should create primarykey?
        database = DATABASE


class Task(Model):
    taskname = CharField()
    priority = CharField()
    saved = BooleanField(default=False)
    created = DateTimeField()
    body = CharField()
    user_id = IntegerField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Task], safe=True)
    print("TABLES created")
    DATABASE.close()
