from app.repositories import QuestionRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Question, QuestionIn, QuestionOut
from typing import List, Optional

class QuestionController(BaseController[Question]):
    def __init__(self, question_repository: QuestionRepository):
        super().__init__(model=Question, repository=question_repository)

    def create_question(self, question_in: QuestionIn) -> QuestionOut:
        return self.repository.create_question(question_in)

    def get_question(self, question_id: int) -> Optional[QuestionOut]:
        return self.repository.get_question(question_id)

    def get_all_questions(self) -> List[QuestionOut]:
        return self.repository.get_all_questions()

    def update_question(self, question_id: int, question_in: QuestionIn) -> Optional[QuestionOut]:
        return self.repository.update_question(question_id, question_in)

    def delete_question(self, question_id: int) -> bool:
        return self.repository.delete_question(question_id)
