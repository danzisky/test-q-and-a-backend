from fastapi import APIRouter, Depends, HTTPException
from app.controllers import FeedbackController  # Import the FeedbackController
from app.schemas.quiz.schema import FeedbackIn, FeedbackOut, Feedback as FeedbackSchema
from typing import List
from core.factory import Factory

feedback_router = APIRouter()

@feedback_router.get("/")
async def get_all_feedbacks(controller: FeedbackController = Depends(Factory().get_feedback_controller)) -> list[FeedbackOut]:
    return await controller.repository.get_all()

@feedback_router.get("/{id}")
async def get_feedback(id: int, controller: FeedbackController = Depends(Factory().get_feedback_controller)) -> FeedbackOut:
    feedback = await controller.get_by_id(id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback

@feedback_router.post("/")
async def create_feedback(feedback: FeedbackIn, controller: FeedbackController = Depends(Factory().get_feedback_controller)):
    return await controller.add(feedback)

@feedback_router.put("/{id}")
async def update_feedback(id: int, feedback: FeedbackIn, controller: FeedbackController = Depends(Factory().get_feedback_controller)):
    return await controller.update(id, feedback)

@feedback_router.delete("/{id}")
async def delete_feedback(id: int, controller: FeedbackController = Depends(Factory().get_feedback_controller)):
    await controller.delete(id)
    return {"message": "Feedback deleted successfully"}
