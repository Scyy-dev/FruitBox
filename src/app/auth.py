from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# Intentionally insecure database for testing purposes
fake_user_db = {
    "admin": {
        "username": "admin",
        "password": "admin"
    },
    "user1": {
        "username": "user1",
        "password": "user1"
    }
}

class User(BaseModel):
    username: str
    password: str
    

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    if token in fake_user_db:
        user_data = fake_user_db[token]
        return User(**user_data)

async def hash_password(password):
    return "temp_salt" + password + "temp_salt"

@router.get("/")
async def auth_user(current_user: Annotated[str, Depends(get_current_user)]):
    return current_user

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_data = fake_user_db.get(form_data.username)
    if not user_data:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = User(**user_data)
    hashed_password = hash_password(form_data.password)
    if not hashed_password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}