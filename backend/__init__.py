from fastapi import (FastAPI,
                     APIRouter)
                     
from .routes import article_router


app = FastAPI()
api_router = APIRouter(prefix="/api")
api_router.include_router(article_router)
app.include_router(api_router)