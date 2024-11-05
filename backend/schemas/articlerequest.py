from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional, Tuple


class ArticleRequest(BaseModel):
    keywords: List[str] = Field(
        ...,
        example=["AI", "Technology"],
        description="List of keywords for searching articles",
    )
    data_range: Optional[Tuple[date, date]] = Field(
        None,
        description="Tuple containing start and end dates for filtering articles by the date",
    )
