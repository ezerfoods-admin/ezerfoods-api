from fastapi import APIRouter
from app.api.routes.index import router as index

router = APIRouter()

router.include_router(index, prefix="/home", tags=["home"])
