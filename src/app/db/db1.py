import os
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str

class FruitDB():
    def __init__(self, connection_url) -> None:
        engine = create_engine(connection_url, echo=True)
        SQLModel.metadata.create_all(engine)
