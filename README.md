* [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) + [Strawberry](https://strawberry.rocks/docs) + SQLite
* Async API server + RDBMS + GraphQL

Run FastAPI
* `uvicorn main:fastapi_app --reload --port 8081`

Run Strawberry
* `strawberry server schema`


```
{
  book {
    title
    author {
      lastName
    }
    year
  }
}
```

```
{
  "data": {
    "book": [
      {
        "title": "The Invisible Man",
        "author": {
          "lastName": "Wells"
        },
        "year": 1897
      },
      {
        "title": "The Island of Dr. Moreau",
        "author": {
          "lastName": "Wells"
        },
        "year": 1896
      },
      {
        "title": "Mrs. Dalloway",
        "author": {
          "lastName": "Woolf"
        },
        "year": 1925
      },
      {
        "title": "To the Lighthouse",
        "author": {
          "lastName": "Woolf"
        },
        "year": 1927
      },
      {
        "title": "Ulysses",
        "author": {
          "lastName": "Joyce"
        },
        "year": 1922
      },
      {
        "title": "Dubliners",
        "author": {
          "lastName": "Joyce"
        },
        "year": 1914
      }
    ]
  }
}
```