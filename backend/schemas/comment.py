from pydantic import BaseModel, Field, ValidationError, field_validator

from typing import Optional

from author import Author

from datetime import datetime


class Comment(BaseModel):
    author: Author = Field(..., description="The author of the comment")
    content: Optional[str] = Field(None, description="The content of the comment")
    created_at: Optional[datetime] = datetime.now

    @field_validator("created_at")
    def future_check(cls, date):
        if date > datetime.now:
            return ValueError("Publishing date cannot be in the future")
        return date