import random

from tortoise import Tortoise
from faker import Faker

from core.database.models import Category
from core.database.models import User
from core.database.models import Quiz
from core.database.models import Question
from core.database.models import Answer
from core.database.models import Result
from core.database.models import Session
from core.database.models import Feedback
from core.database.config import TORTOISE_ORM



# Initialize the Faker instance
fake = Faker()

async def populate_models():
    await Tortoise.init(config=TORTOISE_ORM)


    # Generate fake data and populate models
    for _ in range(10):  # Adjust the number of records as needed
        user = await User.create(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
        )

        category = await Category.create(
            name=fake.word(),
        )

        quiz = await Quiz.create(
            title=fake.sentence(),
            description=fake.text(),
            category=category,
            difficulty=fake.random_element(elements=('Easy', 'Medium', 'Hard')),
            owner=user,
        )

        question = await Question.create(
            question_text=fake.sentence(),
            options=','.join([fake.word() for _ in range(4)]),
            correct_answer=fake.random_element(elements=(1, 2, 3, 4)),
            quiz=quiz,
        )

        answer = await Answer.create(
            answer=fake.word(),
            question=question,
            user=user,
        )

        result = await Result.create(
            score=random.randint(0, 100),
            time_taken=fake.time(),
            user=user,
            quiz=quiz,
        )

        session = await Session.create(
            start_time=fake.date_time().isoformat(),
            end_time=fake.date_time().isoformat(),
            user=user,
        )

        feedback = await Feedback.create(
            feedback_text=fake.text(),
            user=user,
        )

    await Tortoise.close_connections()

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(populate_models())
