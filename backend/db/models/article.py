from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base, PublishedMixin


class Article(Base, PublishedMixin):
    __tablename__ = "articles"
    title: Mapped[str]
    content: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="articles")
    tags: Mapped[str] = mapped_column(default=[])
