from app.repositories import QuizRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Quiz


class QuizController(BaseController[Quiz]):
    def __init__(self, quiz_repository: QuizRepository):
        super().__init__(model=Quiz, repository=quiz_repository)
