from app.repositories import UserRepository
from core.controller import BaseController
from app.schemas.quiz.schema import User


class UserController(BaseController[User]):
    def __init__(self, user_repository: UserRepository):
        super().__init__(model=User, repository=user_repository)
