from fastapi import APIRouter

from .session import session_router

sessions_router = APIRouter()
sessions_router.include_router(session_router, tags=["Session"])

__all__ = ["sessions_router"]
