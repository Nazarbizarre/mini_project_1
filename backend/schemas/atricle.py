from pydantic import BaseModel, Field, field_validator, ValidationError

from typing import Optional

from .author import AuthorData

from datetime import datetime

from ..logging.loggers import validations_logger



class ArticleData(BaseModel):
    title: str = Field(..., description="The title of the article")
    content: str = Field(..., description="The main content of the article")
    author: AuthorData = Field(..., description="The author of the article")
    tags: Optional[list] = Field(
        None, description="List of tags related to the article"
    )
    published_at: Optional[datetime] = Field(
        datetime.now, description="The publication date and time of the article"
    )

    @field_validator("published_at")
    def future_check(cls, date):
        if date > datetime.now():
            validations_logger.info("Model: ArticleData, Field: published_at, Result: Failed (date in future)")
            return ValueError("Publishing date cannot be in the future")
        validations_logger.info("Model: ArticleData, Field: published_at, Result: Success")
        return date
