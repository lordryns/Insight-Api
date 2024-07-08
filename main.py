from fastapi import FastAPI
import json 

app = FastAPI()

# Load bad words from JSON file
with open("profanities.json", 'r') as fp:
    bad_json = json.load(fp)

BAD_WORDS = bad_json["words"]

@app.get("/")
def home():
    return {"title": "Insight Api"}

@app.get("/purify/{text}")
async def purge_text(text: str) -> dict:
    new_text = text

    for word in BAD_WORDS:
        new_text = new_text.replace(word.lower(), '*' * len(word))
        
    return {"text": text,  "purified_string": new_text}
