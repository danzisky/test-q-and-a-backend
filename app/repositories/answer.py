from app.schemas.quiz.schema import Answer, AnswerIn, AnswerOut
from core.repository.base import BaseRepository
from core.database import models

class AnswerRepository(BaseRepository[Answer]):
    def __init__(self):
        super().__init__(schema=AnswerOut, create_schema=AnswerIn, db_model=models.Answer)