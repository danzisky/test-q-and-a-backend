from fastapi import APIRouter

from .feedback import feedback_router

quiz_feedback_router = APIRouter()
quiz_feedback_router.include_router(feedback_router, tags=["Feedback"])

__all__ = ["quiz_feedback_router"]
