import sqlite3
import json
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from schema import schema

graphql_app = GraphQL(schema)

fastapi_app = FastAPI()
fastapi_app.add_route("/graphql", graphql_app)
fastapi_app.add_route("/graphql", graphql_app)
fastapi_app.add_websocket_route("/graphql", graphql_app)

@fastapi_app.get("/book")
async def root():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    res = []
    for row in cur.execute("SELECT * FROM book"):
        res.append({
            "id": row[0],
            "title": row[1],
            "year": row[2],
            "author": row[3]
        })
    return json.dumps(res)

@fastapi_app.get("/author")
async def root():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    res = []
    for row in cur.execute("SELECT * FROM author"):
        res.append({
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2]
        })
    return json.dumps(res)
