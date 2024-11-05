from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base, PublishedMixin


class Author(Base, PublishedMixin):
    __tablename__ = "authors"
    name: Mapped[str]
    email: Mapped[str]
    bio: Mapped[str]
    hashed_password: Mapped[str]
    articles: Mapped[List["Article"]] = relationship(back_populates="author")
