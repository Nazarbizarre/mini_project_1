from pydantic import BaseModel, Field, field_validator, ValidationError

from typing import Optional

from author import Author

from datetime import datetime


class Article(BaseModel):
    title: str = Field(..., description="The title of the article")
    content: str = Field(..., description="The main content of the article")
    author: Author = Field(..., description="The author of the article")
    tags: Optional[list] = Field(
        None, description="List of tags related to the article"
    )
    published_at: Optional[datetime] = Field(
        datetime.now, description="The publication date and time of the article"
    )

    @field_validator("published_at")
    def future_check(cls, date):
        if date > datetime.now:
            return ValueError("Publishing date cannot be in the future")
        return date
