from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "Carlos"}}


@app.get("/about/{id}")
def about(id):
    return {"data": id}
