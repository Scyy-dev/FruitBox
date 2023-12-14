from sqlmodel import Field, SQLModel

class UserBase(SQLModel):
    username: str
    hashed_password: str

class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)