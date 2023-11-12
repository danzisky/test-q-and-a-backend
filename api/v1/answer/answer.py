from fastapi import APIRouter, Depends, HTTPException
from app.controllers import AnswerController
from app.schemas.quiz.schema import AnswerIn, AnswerOut, Answer as AnswerSchema
from typing import List
from core.factory import Factory

answer_router = APIRouter()

@answer_router.get("/")
async def get_all_answers(controller: AnswerController = Depends(Factory().get_answer_controller)) -> list[AnswerOut]:
    return await controller.get_all()

@answer_router.get("/{id}")
async def get_answer(id: int, controller: AnswerController = Depends(Factory().get_answer_controller))  -> AnswerOut:
    answer = await controller.get_by_id(id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer

@answer_router.post("/")
async def create_answer(answer: AnswerIn, controller: AnswerController = Depends(Factory().get_answer_controller)):
    return await controller.add(answer)

@answer_router.put("/{id}")
async def update_answer(id: int, answer: AnswerIn, controller: AnswerController = Depends(Factory().get_answer_controller)):
    return await controller.update(id, answer)

@answer_router.delete("/{id}")
async def delete_answer(id: int, controller: AnswerController = Depends(Factory().get_answer_controller)):
    await controller.delete(id)
    return {"message": "Answer deleted successfully"}