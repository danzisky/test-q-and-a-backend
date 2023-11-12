from app.schemas.quiz.schema import Quiz, QuizIn, QuizOut
from core.repository.base import BaseRepository
from core.database import models

class QuizRepository(BaseRepository[Quiz]):
    def __init__(self):
        super().__init__(schema=QuizOut, create_schema=QuizIn, db_model=models.Quiz)