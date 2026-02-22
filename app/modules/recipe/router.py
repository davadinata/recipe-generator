import re
from fastapi.templating import Jinja2Templates
from sys import prefix
from fastapi import APIRouter, Request, Form
from app.utils.openai import client
from .prompt import SYSTEM_PROMPT
import markdown

template = Jinja2Templates(directory="templates")
recipe_router = APIRouter(prefix="/recipe", tags=["recipes"])

@recipe_router.get("/")
def get_recipe(request : Request):
    return template.TemplateResponse("index.html", {"request": request})

@recipe_router.post("/")
def add_ingredients(request : Request, ingredients = Form(None)):
    
    res = client.chat.completions.create(
    model="google/gemini-2.5-flash-lite",
    messages= [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": ingredients}
    ],
    extra_body={"reasoning": {"enabled": True}}
)
    
    result = res.choices[0].message.content
    
    html = markdown.markdown(result)
    
    return template.TemplateResponse("recipe.html", {"request": request, "recipe": html})