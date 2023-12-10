from datetime import datetime, timedelta
from typing import Annotated, Union

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

SECRET_KEY = "dfa51968819864861db7b70027064d1cb11d36deeabb4cbaf858f6585380b0b4"
ALGORITHM = "HS256"
TOKEN_EXPIRY = 1440 # 24 hrs
DEFAULT_EXPIRY = 30

# === Exceptions ===
INVALID_CREDENTIALS = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
)
INVALID_PASSWORD_CREDENTIALS = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

# === Testing User DB ===
fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "$2b$12$5WbUfUMaeAW13y.AsQqod.kEs8Z/hUkc8Fpr7WI8Cud7uWjM9UoQC"
    },
    "user1": {
        "username": "user1",
        "hashed_password": "$2b$12$5WbUfUMaeAW13y.AsQqod.kEs8Z/hUkc8Fpr7WI8Cud7uWjM9UoQC"
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class User(BaseModel):
    username: str
    hashed_password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

def get_user(db, username: Union[str, None]):
    if username in db:
        return User(**db[username])
    
def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
    
def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=DEFAULT_EXPIRY)

    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise INVALID_CREDENTIALS
        token_data = TokenData(username=username)
    except JWTError:
        raise INVALID_CREDENTIALS
    user = get_user(fake_user_db, username=token_data.username)
    if not user:
        raise INVALID_CREDENTIALS
    return user
    
@router.post("/token")
async def password_oauth(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(fake_user_db, form_data.username, form_data.password)
    if not user:
        raise INVALID_PASSWORD_CREDENTIALS
    access_token_expires = timedelta(minutes=TOKEN_EXPIRY)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/")
async def auth_user(current_user: Annotated[str, Depends(get_current_user)]):
    return current_user
