from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/components/{component_name}")
def read_item(component_name: str, q: Union[str, None] = None):
    return {"component_name": component_name, "q": q}