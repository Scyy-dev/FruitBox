from contextlib import asynccontextmanager
import os

from fastapi import FastAPI
import auth

from endpoints import fruit_teams, fruit_points
from db.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    connection_url = os.environ["DB_CONNECTION_STRING"]
    await init_db(connection_url)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(fruit_teams.router)
app.include_router(fruit_points.router)
