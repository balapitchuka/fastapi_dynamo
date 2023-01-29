import uvicorn
from fastapi import FastAPI

from app.internal.db import initialize_db

from app.domain.recipes import RecipesDomain
from app.repository.recipes import RecipesRepository
from app.routers.recipes import RecipesRouter


app = FastAPI()

db = initialize_db()
recipes_repository = RecipesRepository(db)
recipes_domain = RecipesDomain(recipes_repository)
recipes_router = RecipesRouter(recipes_domain)

app.include_router(recipes_router.router)


@app.get('/')
def index():
    return 'Hello World!'