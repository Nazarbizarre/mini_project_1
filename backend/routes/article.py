from fastapi import APIRouter, status

from ..schemas import Article


article_router = APIRouter(prefix="/article")


@article_router.get("/", summary="Test Endpoint")
def index():
    return {"Hello From ": "Article Router"}


@article_router.post(
    "/create", summary="Create Article", status_code=status.HTTP_201_CREATED
)
def create_article(data: Article):
    pass
