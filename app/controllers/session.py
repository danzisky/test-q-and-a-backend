from app.repositories import SessionRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Session

class SessionController(BaseController[Session]):
    def __init__(self, session_repository: SessionRepository):
        super().__init__(model=Session, repository=session_repository)
