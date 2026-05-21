from fastapi import APIRouter
from .repo import router as repo_router

router = APIRouter()

router.include_router(repo_router)