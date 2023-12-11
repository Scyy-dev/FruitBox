from os import environ

from sqlmodel import SQLModel, Session, create_engine  # noqa: F401 - used as part of import
from . import models

engine = create_engine(environ["DB_CONNECTION_STRING"], echo=True)

async def test_db():
    user1 = models.User(username="admin", hashed_password="$2b$12$5WbUfUMaeAW13y.AsQqod.kEs8Z/hUkc8Fpr7WI8Cud7uWjM9UoQC")
    with Session(engine) as session:
        session.add(user1)