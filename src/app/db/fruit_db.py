from typing import Optional
from os import environ

from sqlmodel import Field, SQLModel, Session, create_engine

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str

engine = create_engine(environ["DB_CONNECTION_STRING"], echo=True)

def main():
    SQLModel.metadata.create_all(engine)
    user1 = User(id=None, username="admin", hashed_password="$2b$12$5WbUfUMaeAW13y.AsQqod.kEs8Z/hUkc8Fpr7WI8Cud7uWjM9UoQC")
    with Session(engine) as session:
        session.add(user1)

if __name__ == "__main__":
    main()
