from fastapi import APIRouter

from .monitoring import monitoring_router
from .answer import answers_router
from .category import categories_router
from .feedback import quiz_feedback_router
from .question import questions_router
from .quiz import quizzes_router
from .result import results_router
from .session import sessions_router
from .user import users_router


v1_router = APIRouter()
v1_router.include_router(monitoring_router, prefix="/monitoring")
v1_router.include_router(answers_router, prefix="/answer")
v1_router.include_router(categories_router, prefix="/category")
v1_router.include_router(quiz_feedback_router, prefix="/feedback")
v1_router.include_router(questions_router, prefix="/question")
v1_router.include_router(quizzes_router, prefix="/quiz")
v1_router.include_router(results_router, prefix="/result")
v1_router.include_router(sessions_router, prefix="/session")
v1_router.include_router(users_router, prefix="/user")


