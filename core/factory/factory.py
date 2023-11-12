from functools import partial
from fastapi import Depends
from app.controllers import AnswerController, CategoryController, FeedbackController, QuestionController, QuizController, ResultController, SessionController, UserController

from app.repositories.answer import AnswerRepository
from app.repositories.category import CategoryRepository
from app.repositories.feedback import FeedbackRepository
from app.repositories.question import QuestionRepository
from app.repositories.quiz import QuizRepository
from app.repositories.result import ResultRepository
from app.repositories.session import SessionRepository
from app.repositories.user import UserRepository

class Factory:
    """
    This is the factory container that will instantiate all the controllers and
    repositories which can be accessed by the rest of the application.
    """

    def get_answer_controller(self):
        return AnswerController(
            answer_repository=AnswerRepository()
        )

    def get_category_controller(self):
        return CategoryController(
            category_repository=CategoryRepository()
        )

    def get_feedback_controller(self):
        return FeedbackController(
            feedback_repository=FeedbackRepository()
        )

    def get_question_controller(self):
        return QuestionController(
            question_repository=QuestionRepository()
        )

    def get_quiz_controller(self):
        return QuizController(
            quiz_repository=QuizRepository()
        )

    def get_result_controller(self):
        return ResultController(
            result_repository=ResultRepository()
        )

    def get_session_controller(self):
        return SessionController(
            session_repository=SessionRepository()
        )
    
    def get_user_controller(self):
        return UserController(
            user_repository=UserRepository()
        )

    # Repositories
    answer_repository = partial(AnswerRepository)
    category_repository = partial(CategoryRepository)
    feedback_repository = partial(FeedbackRepository)
    question_repository = partial(QuestionRepository)
    quiz_repository = partial(QuizRepository)
    result_repository = partial(ResultRepository)
    session_repository = partial(SessionRepository)
    user_repository = partial(UserRepository)
