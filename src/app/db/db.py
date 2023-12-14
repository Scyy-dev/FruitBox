import asyncio
from sqlmodel import SQLModel, create_engine

class FruitDB():
    def connect(self, conn_str: str):
        if not conn_str:
            return False
        
        self._conn_str = conn_str
        self._db = create_engine(self._conn_str, echo=True)
        SQLModel.metadata.create_all(self._db)

    def health_check(self):
        return self._db is not None
    
async def init_db(conn_str):
    while True:
        try:
            print("attempting DB connection...")
            db.connect(conn_str)
            break
        except Exception as e:
            print("Connection failed:", e)
            await asyncio.sleep(2)

db = FruitDB()