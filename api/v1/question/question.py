from fastapi import APIRouter, Depends, HTTPException
from app.controllers import QuestionController  
from app.schemas.quiz.schema import QuestionIn, QuestionOut, Question as QuestionSchema
from typing import List
from core.factory import Factory

question_router = APIRouter()

@question_router.get("/")
async def get_all_questions(controller: QuestionController = Depends(Factory().get_question_controller)) -> list[QuestionOut]:
    return await controller.repository.get_all()

@question_router.get("/{id}")
async def get_question(id: int, controller: QuestionController = Depends(Factory().get_question_controller)) -> QuestionOut:
    question = await controller.get_by_id(id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@question_router.post("/")
async def create_question(question: QuestionIn, controller: QuestionController = Depends(Factory().get_question_controller)) -> QuestionOut:
    return await controller.add(question)

@question_router.put("/{id}", response_model=QuestionOut)
async def update_question(id: int, question: QuestionIn, controller: QuestionController = Depends(Factory().get_question_controller)):
    return await controller.update(id, question)

@question_router.delete("/{id}")
async def delete_question(id: int, controller: QuestionController = Depends(Factory().get_question_controller)):
    await controller.delete(id)
    return {"message": "Question deleted successfully"}
