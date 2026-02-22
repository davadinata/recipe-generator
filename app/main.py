from app.modules.recipe.router import recipe_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(recipe_router)