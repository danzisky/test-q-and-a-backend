from app.schemas.quiz.schema import User, UserOut, UserIn
from core.repository.base import BaseRepository
from core.database import models

class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(schema=UserOut, create_schema=UserIn, db_model=models.User)