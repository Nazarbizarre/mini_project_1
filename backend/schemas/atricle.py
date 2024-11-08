from datetime import datetime
from typing import Optional

from pydantic import (BaseModel,
                      Field,
                      field_validator,
                      ValidationError)

from .author import AuthorData



class ArticleData(BaseModel):
    title: str = Field(..., description="The title of the article")
    content: str = Field(..., description="The main content of the article")
    tags: Optional[str] = Field(
        None, description="String of tags related to the article"
    )
    published_at: Optional[datetime] = Field(
        default_factory=datetime.now,
        description="The publication date and time of the article",
    )

    @field_validator("published_at")
    def future_check(cls, date):
        if date > datetime.now():
            raise ValueError("Publishing date cannot be in the future")
        return date
