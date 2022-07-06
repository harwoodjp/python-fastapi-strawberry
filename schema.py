from typing import List
import strawberry
import sqlite3

@strawberry.type
class Book:
    id: int
    title: str
    year: int
    author: 'Author'

@strawberry.type
class Author:
    id: int
    first_name: str
    last_name: str

@strawberry.type
class Query:
    @strawberry.field
    def book(self) -> List[Book]:
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        books = []
        for row in cur.execute("SELECT * FROM book"):
            cur2 = con.cursor()
            for row2 in cur2.execute(f"SELECT * FROM author WHERE id = {row[3]}"):
                book = Book(row[0], row[1], row[2], Author(row2[0], row2[1], row2[2]))
                books.append(book)
        return books

    @strawberry.field
    def author(self) -> List[Author]:
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        authors = []
        for row in cur.execute("SELECT * FROM author"):
            author = Author(row[0], row[1], row[2])
            authors.append(author)
        return authors

schema = strawberry.Schema(query=Query)


