from fastapi import FastAPI
import json 

with open("profanities.json", 'r') as fp:
    bad_json = json.load(fp)

BAD_WORDS = bad_json["words"]


app = FastAPI()

@app.get("/")
def home():
    return {"title": "Inisight Api"}


@app.get("/purify/{text}")
async def purge_text(text: str) -> dict:
    new_text = ""

    for words in BAD_WORDS:
        new_text = text.replace(words, "****")
    return {"text": text, "purified_string": new_text}