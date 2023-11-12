from typing import Optional
from pydantic import BaseModel
from tortoise import Tortoise
Tortoise.init_models(["core.database.models"], "models")

from core.database.models import User as UserModel
from core.database.models import Quiz as QuizModel
from core.database.models import Question as QuestionModel
from core.database.models import Answer as AnswerModel
from core.database.models import Result as ResultModel
from core.database.models import Category as CategoryModel
from core.database.models import Session as SessionModel
from core.database.models import Feedback as FeedbackModel
from tortoise.contrib.pydantic import pydantic_model_creator


UserIn = pydantic_model_creator(UserModel, name="UserIn", exclude_readonly=True)
UserOut = pydantic_model_creator(UserModel, name="UserOut")

QuizIn = pydantic_model_creator(QuizModel, name="QuizIn", exclude_readonly=True)
QuizOut = pydantic_model_creator(QuizModel, name="QuizOut")

QuestionIn = pydantic_model_creator(QuestionModel, name="QuestionIn", exclude_readonly=True)
QuestionOut = pydantic_model_creator(QuestionModel, name="QuestionOut")

AnswerIn = pydantic_model_creator(
    AnswerModel,
    name="AnswerIn",
    exclude_readonly=True
)


AnswerOut = pydantic_model_creator(AnswerModel, name="AnswerOut")

ResultIn = pydantic_model_creator(ResultModel, name="ResultIn", exclude_readonly=True)
ResultOut = pydantic_model_creator(ResultModel, name="ResultOut")

CategoryIn = pydantic_model_creator(CategoryModel, name="CategoryIn", exclude_readonly=True)
CategoryOut = pydantic_model_creator(CategoryModel, name="CategoryOut")

SessionIn = pydantic_model_creator(SessionModel, name="SessionIn", exclude_readonly=True)
SessionOut = pydantic_model_creator(SessionModel, name="SessionOut")

FeedbackIn = pydantic_model_creator(FeedbackModel, name="FeedbackIn", exclude_readonly=True)
FeedbackOut = pydantic_model_creator(FeedbackModel, name="FeedbackOut")

class User(BaseModel):
    username: str
    email: Optional[str] = None
    password: str

class Quiz(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    category: str
    difficulty: str
    owner_id: int

class Question(BaseModel):
    id: int
    question_text: str
    options: str
    correct_answer: str
    quiz_id: int

class Answer(BaseModel):
    id: int
    answer: str
    question_id: int
    user_id: int

class Result(BaseModel):
    id: int
    score: int
    time_taken: str
    user_id: int
    quiz_id: int

class Category(BaseModel):
    id: int
    name: str

class Session(BaseModel):
    id: int
    start_time: str
    end_time: str
    user_id: int

class Feedback(BaseModel):
    id: int
    feedback_text: str
    user_id: int

