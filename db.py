import datetime
import uuid
from peewee import *

db = SqliteDatabase("db2.db")

class BaseModel(Model):
    uid = uuid.uuid4().hex
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db

class Author(BaseModel):
    first_name = TextField()
    last_name = TextField()

class Book(BaseModel):
    title = TextField()
    year = TextField()
    author = ForeignKeyField(Author, backref="authors")
    pass

def seed():
    data = [
        {
            "author": {
                "first_name": "James",
                "last_name": "Joyce",
                "books": [
                    {
                        "title": "Ulysses",
                        "year": "1922"
                    },
                    {
                        "title": "Dubliners",
                        "year": "1914"
                    }
                ]
            }
        }
    ]
    for datum in data:
        author = Author.create(
            first_name = datum["author"]["first_name"],
            last_name = datum["author"]["last_name"]
        )
        for book in datum["author"]["books"]:
            Book.create(
                title = book["title"],
                year = book["year"],
                author = author
            )
