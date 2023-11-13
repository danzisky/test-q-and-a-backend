from app.repositories import QuizRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Quiz, QuizIn, QuizOut
from typing import List

class QuizController(BaseController):
    def __init__(self, quiz_repository: QuizRepository):
        super().__init__(model=Quiz, repository=quiz_repository)

    async def get_all(self) -> List[QuizOut]:
        return await self.repository.get_all()

    async def get_by_id(self, quiz_id: int) -> QuizOut:
        return await self.repository.get_by_id(quiz_id)

    async def add(self, quiz_in: QuizIn) -> QuizOut:
        print(quiz_in)
        return await self.repository.add_entity(quiz_in)

    async def update(self, quiz_id: int, quiz_in: QuizIn) -> QuizOut:
        return await self.repository.update_entity(quiz_id, quiz_in)

    async def delete(self, quiz_id: int):
        return await self.repository.delete_entity(quiz_id)
