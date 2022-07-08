import sqlite3
import json
import datetime
import uuid
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from schema import schema
import db

graphql_app = GraphQL(schema)
fastapi_app = FastAPI()
fastapi_app.add_route("/graphql", graphql_app)
fastapi_app.add_websocket_route("/graphql", graphql_app)

@fastapi_app.get("/book")
async def root():
    res = []
    for book in db.Book.select():
        res.append({
            "created_at": book.created_at,
            "updated_at": book.updated_at,
            "uid": book.uid,
            "id": book.id,
            "title": book.title,
            "year": book.year
        })
    return json.dumps(res, default=str)


@fastapi_app.get("/author")
async def root():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    res = []
    for author in db.Author.select():
        res.append({
            "created_at": author.created_at,
            "updated_at": author.updated_at,
            "uid": author.uid,
            "id": author.id,
            "first_name": author.first_name,
            "last_name": author.last_name
        })
    return json.dumps(res, default=str)
