from fastapi import APIRouter

from .question import question_router

questions_router = APIRouter()
questions_router.include_router(question_router, tags=["Question"])

__all__ = ["questions_router"]
