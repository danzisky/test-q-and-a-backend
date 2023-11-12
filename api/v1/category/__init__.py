from fastapi import APIRouter

from .category import category_router

categories_router = APIRouter()
categories_router.include_router(category_router, tags=["Category"])


__all__ = ["categories_router"]
