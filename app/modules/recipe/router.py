from sys import prefix
from fastapi import APIRouter


recipe_router = APIRouter(prefix="/recipes", tags=["recipes"])

@recipe_router.get("/")
def get_recipe():
    pass