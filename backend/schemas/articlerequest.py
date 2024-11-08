from pydantic import (BaseModel,
                      Field)
from datetime import datetime
from typing import (List,
                    Optional,
                    Tuple)


class DateRange(BaseModel):
    start: datetime
    end: datetime


class ArticleRequest(BaseModel):
    keywords: List[str] = Field(
        ..., description="List of keywords for searching articles."
    )
    date_range: DateRange
