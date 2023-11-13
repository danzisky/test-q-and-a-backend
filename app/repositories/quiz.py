from app.schemas.quiz.schema import Quiz, QuizIn, QuizOut
from core.repository.base import BaseRepository
from core.exceptions import NotFoundException
from tortoise.queryset import QuerySet
from core.database import models
from tortoise import Tortoise

class QuizRepository(BaseRepository[Quiz]):
    def __init__(self):
        super().__init__(schema=QuizOut, create_schema=QuizIn, db_model=models.Quiz)

    async def get_all(self) -> QuerySet[Quiz]:
        return await super().get_all()

    async def get_by_id(self, quiz_id: int) -> Quiz:
        try:
            return await super().get_by_id(quiz_id)
        except models.Quiz.DoesNotExist:
            raise NotFoundException(f"Quiz with id {quiz_id} not found")

    async def add_entity(self, quiz_in: QuizIn) -> Quiz:
        try:
            return await super().add_entity(quiz_in)
        except Exception as e:
            # Handle specific exceptions (e.g., IntegrityError) as needed
            raise Exception(f"Failed to add quiz: {str(e)}")

    async def update_entity(self, quiz_id: int, quiz_in: QuizIn) -> Quiz:
        try:
            return await super().update_entity(quiz_id, quiz_in)
        except models.Quiz.DoesNotExist:
            raise NotFoundException(f"Quiz with id {quiz_id} not found")
        except Exception as e:
            # Handle specific exceptions (e.g., IntegrityError) as needed
            raise Exception(f"Failed to update quiz: {str(e)}")

    async def delete_entity(self, quiz_id: int):
        try:
            await super().delete_entity(quiz_id)
        except models.Quiz.DoesNotExist:
            raise NotFoundException(f"Quiz with id {quiz_id} not found")
        except Exception as e:
            # Handle specific exceptions (e.g., IntegrityError) as needed
            raise Exception(f"Failed to delete quiz: {str(e)}")
