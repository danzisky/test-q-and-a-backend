from app.repositories import ResultRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Result


class ResultController(BaseController[Result]):
    def __init__(self, result_repository: ResultRepository):
        super().__init__(model=Result, repository=result_repository)
