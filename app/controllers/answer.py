from app.repositories import AnswerRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Answer


class AnswerController(BaseController[Answer]):
    def __init__(self, answer_repository: AnswerRepository):
        super().__init__(model=Answer, repository=answer_repository)
