from fastapi import APIRouter, Depends, HTTPException
from app.controllers import ResultController  # Import the ResultController
from app.schemas.quiz.schema import ResultIn, ResultOut, Result as ResultSchema
from typing import List
from core.factory import Factory

result_router = APIRouter()

@result_router.get("/")
async def get_all_results(controller: ResultController = Depends(Factory().get_result_controller)) -> list[ResultOut]:
    return await controller.repository.get_all()

@result_router.get("/{id}")
async def get_result(id: int, controller: ResultController = Depends(Factory().get_result_controller)) -> ResultOut:
    result = await controller.get_by_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")
    return result

@result_router.post("/")
async def create_result(result: ResultIn, controller: ResultController = Depends(Factory().get_result_controller)) -> ResultOut:
    return await controller.add(result)

@result_router.put("/{id}")
async def update_result(id: int, result: ResultIn, controller: ResultController = Depends(Factory().get_result_controller)) -> ResultOut:
    return await controller.update(id, result)

@result_router.delete("/{id}")
async def delete_result(id: int, controller: ResultController = Depends(Factory().get_result_controller)):
    await controller.delete(id)
    return {"message": "Result deleted successfully"}
