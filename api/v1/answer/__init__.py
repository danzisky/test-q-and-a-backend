from fastapi import APIRouter

from .answer import answer_router

answers_router = APIRouter()
answers_router.include_router(answer_router, tags=["Answer"])

__all__ = ["answers_router"]