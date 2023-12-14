from fastapi import FastAPI
import auth
from endpoints import fruit_teams, fruit_points
from db.db1 import engine

app = FastAPI()

app.include_router(auth.router)
app.include_router(fruit_teams.router)
app.include_router(fruit_points.router)