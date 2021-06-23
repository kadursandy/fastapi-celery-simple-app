from fastapi import FastAPI
from pydantic import BaseModel

from worker import add

app = FastAPI(docs_url="/")


class Numbers(BaseModel):
    a: float = 1
    b: float = 1


@app.get("/hello")
def hello():
    return {"result": "World!!"}


@app.post("/add")
def add_two_numbers(n: Numbers):
    add.delay(n.a, n.b)

