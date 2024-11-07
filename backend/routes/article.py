from typing import Annotated, List

from sqlalchemy import select, update
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, HTTPException

from ..schemas import ArticleData, ArticleRequest
from ..utils import OAUTH2_SCHEME, get_current_user
from ..db import Article, AsyncDB, Author


article_router = APIRouter(prefix="/article", tags=["articles"])


@article_router.post("/", status_code=status.HTTP_201_CREATED, summary = "Crete new article", description = "Create mew article (ArticleData schema)")
async def create_article(
    data: ArticleData,
    current_user: Annotated[Author, Depends(get_current_user)],
    session: Annotated[Session, Depends(AsyncDB.get_session)],
):
    article = Article(**data.model_dump(), author_id=current_user.id)
    session.add(article)


@article_router.post("/filter", response_model=List[ArticleData])
async def filter_articles(
    request: ArticleRequest, session: Annotated[Session, Depends(AsyncDB.get_session)]
):
    articles = (
        session.query(Article)
        .filter(
            Article.published_at >= request.date_range.start,
            Article.published_at <= request.date_range.end,
        )
        .all()
    )
    filtered_articles = [
        article
        for article in articles
        if article.tags
        and any(keyword.lower() in article.tags.lower() for keyword in request.keywords)
    ]
    return filtered_articles


@article_router.get("/", summary = "Articles", description = "Return all user articles")
async def get_user_articles(
    current_user: Annotated[Author, Depends(get_current_user)],
    session: Annotated[Session, Depends(AsyncDB.get_session)],
):
    articles = session.scalars(
        select(Article).where(Article.author_id == current_user.id)
    ).all()
    # articles = [ArticleData.model_validate(article) for article in articles]
    return articles


@article_router.delete("/{article_id}", summary = "Delete article", description = "Delete user article by id")
async def delete_article(
    article_id: int,
    current_user: Annotated[Author, Depends(get_current_user)],
    session: Annotated[Session, Depends(AsyncDB.get_session)],
):
    article = session.scalar(select(Article).where(Article.id == article_id))
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")

    if article.author_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to delete this article"
        )
    session.delete(article)
    return article



@article_router.put("/edit", summary = "Edit article", description = "Delete user own article by id")
async def edit_article(
    article_id: int,
    data: ArticleData,
    current_user: Annotated[Author, Depends(get_current_user)],
    session: Annotated[Session, Depends(AsyncDB.get_session)],
):
    article = session.scalar(select(Article).where(Article.id == article_id))
    if article is None:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Article not found"
        )
    if article.author_id != current_user.id:
        raise HTTPException (
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "You do not have permission for this action"
        )
    article.title = data.title
    article.content = data.content
    article.author_id = current_user.id
    article.tags = data.tags
    article.published_at = data.published_at


    session.merge(article)
    return article