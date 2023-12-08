from fastapi import FastAPI
from .endpoints import fruit_teams, fruit_points

app = FastAPI()

app.include_router(fruit_teams.router)
app.include_router(fruit_points.router)
