from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

TEMP_SALT = "temp-salt"

# Intentionally insecure database for testing purposes
fake_user_db = {
    "admin": {
        "username": "admin",
        "password": TEMP_SALT + "admin" + TEMP_SALT
    },
    "user1": {
        "username": "user1",
        "password": TEMP_SALT + "user1" + TEMP_SALT
    }
}

class User(BaseModel):
    username: str
    password: str
    

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    if token in fake_user_db:
        user_data = fake_user_db[token]
        return User(**user_data)

async def hash_password(password):
    return TEMP_SALT + password + TEMP_SALT

@router.get("/")
async def auth_user(current_user: Annotated[str, Depends(get_current_user)]):
    return current_user

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_data = fake_user_db.get(form_data.username)
    print("user_data:", user_data)
    if not user_data:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = User(**user_data)
    print("user:", user)
    hashed_password = await hash_password(form_data.password)
    print("hashed pw:", hashed_password)
    if not hashed_password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}