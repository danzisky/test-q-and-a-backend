from app.repositories import FeedbackRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Feedback

class FeedbackController(BaseController[Feedback]):
    def __init__(self, feedback_repository: FeedbackRepository):
        super().__init__(model=Feedback, repository=feedback_repository)
