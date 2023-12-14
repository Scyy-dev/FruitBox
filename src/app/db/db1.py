import os
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str

connection_url = os.environ["DB_CONNECTION_STRING"]

engine = create_engine(connection_url, echo=True)

SQLModel.metadata.create_all(engine)