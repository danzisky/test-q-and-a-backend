from app.schemas.quiz.schema import FeedbackIn, FeedbackOut, Feedback
from core.repository.base import BaseRepository
from core.database import models



class FeedbackRepository(BaseRepository[Feedback]):
    def __init__(self):
        super().__init__(schema=FeedbackOut, create_schema=FeedbackIn, db_model=models.Feedback)