from app.modules.recipe.router import recipe_router
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.include_router(recipe_router)