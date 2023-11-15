from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from app.controllers import QuizController  # Import the QuizController
# from app.schemas.quiz.schema import FeedbackIn, FeedbackOut, Feedback as FeedbackSchema
from app.schemas.quiz.schema import QuizIn, QuizOut, Quiz as QuizSchema
from typing import List
from core.factory import Factory
import httpx
from core.database import models

quiz_router = APIRouter()

@quiz_router.get("/")
async def get_all_quizzes(controller: QuizController = Depends(Factory().get_quiz_controller)) -> List[QuizOut]:
    return await controller.repository.get_all()

@quiz_router.get("/{id}")
async def get_quiz(id: int, controller: QuizController = Depends(Factory().get_quiz_controller)) -> QuizOut:
    quiz = await controller.get_by_id(id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@quiz_router.post("/", response_model=QuizOut)
async def create_quiz(quiz: QuizIn, controller: QuizController = Depends(Factory().get_quiz_controller)) -> QuizOut:
    return await controller.add(quiz)

@quiz_router.put("/{id}", response_model=QuizOut)
async def update_quiz(id: int, quiz: QuizIn, controller: QuizController = Depends(Factory().get_quiz_controller)) -> QuizOut:
    return await controller.update(id, quiz)

@quiz_router.delete("/{id}")
async def delete_quiz(id: int, controller: QuizController = Depends(Factory().get_quiz_controller)):  
    await controller.delete(id)
    return {"message": "Quiz deleted successfully"}

@quiz_router.post("/generate_quiz/{category_id}", response_model=QuizOut)
async def generate_quiz(category_id: int, controller: QuizController = Depends(Factory().get_quiz_controller)) -> QuizOut:
    try:
        data = await fetch_quiz()
        quiz_data = data["results"][0]
        quiz = QuizIn(
            title='title',
            category_id=category_id,
            description=quiz_data["question"],
            difficulty="Easy",
            owner_id=38,
        )
        return await controller.add(quiz)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
async def fetch_quiz():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://opentdb.com/api.php?amount=1&type=multiple")
        # print(response.json())
        return response.json()
