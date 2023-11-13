from typing import List, Optional

from app.schemas.quiz.schema import Question, QuestionIn, QuestionOut
from core.repository.base import BaseRepository
from core.database import models

class QuestionRepository(BaseRepository[Question]):
    def __init__(self):
        super().__init__(schema=QuestionOut, create_schema=QuestionIn, db_model=models.Question)

    def create_question(self, question_in: QuestionIn) -> QuestionOut:
        return self.create(question_in)

    def get_question(self, question_id: int) -> Optional[QuestionOut]:
        return self.get(question_id)

    def get_all_questions(self) -> List[QuestionOut]:
        return self.get_all()

    def update_question(self, question_id: int, question_in: QuestionIn) -> Optional[QuestionOut]:
        return self.update(question_id, question_in)

    def delete_question(self, question_id: int) -> bool:
        return self.delete(question_id)
