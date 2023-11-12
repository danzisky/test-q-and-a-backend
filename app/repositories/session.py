from app.schemas.quiz.schema import Session, SessionIn, SessionOut
from core.repository.base import BaseRepository


class SessionRepository(BaseRepository[Session]):
    def __init__(self):
        super().__init__(schema=SessionOut, create_schema=SessionIn, db_model=Session)
