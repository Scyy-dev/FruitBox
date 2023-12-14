import asyncio
from contextlib import asynccontextmanager
import os
from fastapi import FastAPI
import auth
from endpoints import fruit_teams, fruit_points
from db.db import db

app = FastAPI()

app.include_router(auth.router)
app.include_router(fruit_teams.router)
app.include_router(fruit_points.router)

@asynccontextmanager
async def lifecycle(app: FastAPI):
    await init_db()
    yield

async def init_db():
    connection_url = os.environ["DB_CONNECTION_STRING"]
    while True:
        try:
            print("attempting DB connection...")
            db.connect(connection_url)
            break
        except Exception as e:
            print("Connection failed:", e)
            await asyncio.sleep(2)