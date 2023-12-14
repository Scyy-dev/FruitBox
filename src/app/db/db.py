from sqlmodel import SQLModel, Session, create_engine  # noqa: F401 - used as part of import

class FruitDB():
    def connect(self, conn_str: str):
        if not conn_str:
            return False
        
        self._conn_str = conn_str
        self._db = create_engine(self._conn_str, echo=True)
        SQLModel.metadata.create_all(self._db)

    def health_check(self):
        return self._db is not None
    
db = FruitDB()