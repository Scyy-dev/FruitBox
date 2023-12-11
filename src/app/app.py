from fastapi import FastAPI
import auth
from endpoints import fruit_teams, fruit_points
from db.db import engine, SQLModel, test_db

app = FastAPI()

app.include_router(auth.router)
app.include_router(fruit_teams.router)
app.include_router(fruit_points.router)

SQLModel.metadata.create_all(engine)

@app.get("/test_db")
async def test_db_():
    await test_db()