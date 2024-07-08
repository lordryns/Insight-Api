from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"title": "Inisight Api"}


@app.get("/purify/{text}")
async def purge_text(text: str) -> dict:
    return {"text": text, "purified_string": text}