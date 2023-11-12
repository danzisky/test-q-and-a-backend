from app.repositories import CategoryRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Category



class CategoryController(BaseController[Category]):
    def __init__(self, category_repository: CategoryRepository):
        super().__init__(model=Category, repository=category_repository)
