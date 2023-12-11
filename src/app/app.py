from fastapi import FastAPI
import auth
from endpoints import fruit_teams, fruit_points
from db.fruit_db import main as db_main

app = FastAPI()

app.include_router(auth.router)
app.include_router(fruit_teams.router)
app.include_router(fruit_points.router)

@app.get("/test_db")
async def test_db():
    db_main()
