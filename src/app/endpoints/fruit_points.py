from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, Query

# === FastAPI Router ===
router = APIRouter(
    prefix="/fruit_points",
    tags=["fruit_points"]
)