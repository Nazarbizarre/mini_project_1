from typing import Annotated

from fastapi import APIRouter, status, Depends

from ..schemas import ArticleData
from ..utils import OAUTH2_SCHEME
from ..db import Article


article_router = APIRouter(prefix="/article")


@article_router.get(
    "/",
    summary="Test Endpoint",
)
def index(token: Annotated[str, Depends(OAUTH2_SCHEME)]):
    return {"Hello From ": "Article Router"}


@article_router.post(
    "/create", summary="Create Article", status_code=status.HTTP_201_CREATED
)
def create_article(data: ArticleData):
    article = Article(**data.model_dump())
