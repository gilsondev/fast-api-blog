from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    return {"data": f"{limit} blogs from the db"}


@app.get("/blog/{id}")
def about(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int, limit=10):
    return {"data": {"1", "2"}}


@app.post("/blog")
def create_blog(blog: Blog):
    return blog
