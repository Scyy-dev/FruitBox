from sqlmodel import SQLModel, Session, create_engine  # noqa: F401 - used as part of import

from . import models

class FruitDB():

    def __init__(self, conn_str):
        self.init_engine(conn_str)
        SQLModel.metadata.create_all(self._engine)

    def init_engine(self, conn_str):
        self._engine = create_engine(conn_str, echo=True)

    async def test_db(self):
        user1 = models.User(username="admin", hashed_password="$2b$12$5WbUfUMaeAW13y.AsQqod.kEs8Z/hUkc8Fpr7WI8Cud7uWjM9UoQC")
        with Session(self._engine) as session:
            session.add(user1)
    