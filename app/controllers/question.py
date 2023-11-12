from app.repositories import QuestionRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Question


class QuestionController(BaseController[Question]):
    def __init__(self, question_repository: QuestionRepository):
        super().__init__(model=Question, repository=question_repository)
