from fastapi import APIRouter, Depends, HTTPException
from app.controllers import CategoryController
from app.schemas.quiz.schema import CategoryIn, CategoryOut, Category as CategorySchema
from typing import List
from core.factory import Factory

category_router = APIRouter()

@category_router.get("/")
async def get_all_categories(controller: CategoryController = Depends(Factory().get_category_controller)) -> list[CategoryOut]:
    return await controller.repository.get_all()

@category_router.get("/{id}")
async def get_category(id: int, controller: CategoryController = Depends(Factory().get_category_controller)) -> CategoryOut:
    category = await controller.get_by_id(id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@category_router.post("/")
async def create_category(category: CategoryIn, controller: CategoryController = Depends(Factory().get_category_controller)) -> CategoryOut:
    return await controller.add(category)

@category_router.put("/{id}")
async def update_category(id: int, category: CategoryIn, controller: CategoryController = Depends(Factory().get_category_controller)) -> CategoryOut:
    return await controller.update(id, category)

@category_router.delete("/{id}")
async def delete_category(id: int, controller: CategoryController = Depends(Factory().get_category_controller)):
    await controller.delete(id)
    return {"message": "Category deleted successfully"}
