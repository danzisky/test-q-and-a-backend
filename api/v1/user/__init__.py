from fastapi import APIRouter

from .user import user_router

users_router = APIRouter()
users_router.include_router(user_router, tags=["User"])

__all__ = ["users_router"]