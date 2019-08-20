from peewee import *
from flask_login import UserMixin
import datetime  # python module to help deal with dates

DATABASE = SqliteDatabase('tasks.sqlite')


class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    login = DateTimeField(default=datetime.datetime.now)
    logout = DateTimeField(default=datetime.datetime.now)

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
    completed = BooleanField(default=False)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Task], safe=True)
    print("TABLES created")
    DATABASE.close()
