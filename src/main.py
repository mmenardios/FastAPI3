from fastapi import FastAPI
from pydantic import BaseModel

import json
import os

print(os.getcwd())

from utils.embedding import use_embed

class Input(BaseModel):
    text: str


# Define the app
app = FastAPI(
    title="MyAwesomePythonWebApp",
    description="Hello API developer!",
    version="0.1.0"
)


# Define the APIs
@app.get("/")
async def main():
    return {"message": "Hello World"}


# Define a POST operation
@app.post("/submit")
async def submit(input: Input):
    return {"message": f"Data submitted is: {input.text}"}
