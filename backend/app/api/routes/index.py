from typing import List
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def index() -> List[dict]:
    home = [
        {"message": "Welcome to the Homepage"}
    ]

    return home
