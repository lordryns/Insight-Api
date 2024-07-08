from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"title": "Inisight Api"}