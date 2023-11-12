from app.schemas.quiz.schema import Question, QuestionIn, QuestionOut
from core.repository.base import BaseRepository
from core.database import models

class QuestionRepository(BaseRepository[Question]):
    def __init__(self):
        super().__init__(schema=QuestionOut, create_schema=QuestionIn, db_model=models.Question)