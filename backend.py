from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlite3


app = FastAPI(
    docs_url="/docs",
    redoc_url=None,
    title="Seminar hackithon 2024",
)

app.mount("/static", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="./templates")

@app.get("/data")
async def get_data():
    return {"data": "data"}

@app.get("/hello")
async def read_root():
    return "JÁ JSEM ZE SERVERU"

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})