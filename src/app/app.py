from os import environ

from fastapi import FastAPI
import auth
from endpoints import fruit_teams, fruit_points
from db.db import FruitDB

app = FastAPI()

app.include_router(auth.router)
app.include_router(fruit_teams.router)
app.include_router(fruit_points.router)

db = FruitDB(environ["DB_CONNECTION_STRING"])

@app.get("/test_db")
async def test_db_():
    await db.test_db()