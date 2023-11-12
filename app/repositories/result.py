from app.schemas.quiz.schema import Result, ResultIn, ResultOut
from core.repository.base import BaseRepository
from core.database import models

class ResultRepository(BaseRepository[Result]):
    def __init__(self):
        super().__init__(schema=ResultOut, create_schema=ResultIn, db_model=models.Result)

