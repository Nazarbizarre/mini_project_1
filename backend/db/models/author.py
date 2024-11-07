from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base, PublishedMixin


class Author(Base, PublishedMixin):
    __tablename__ = "authors"
    name: Mapped[str]
    email: Mapped[str]
    bio: Mapped[str]
    password: Mapped[str]
    articles: Mapped[List["Article"]] = relationship(back_populates="author")
    comments: Mapped[List["Comment"]] = relationship(back_populates="author")
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    role: Mapped["Role"] = relationship(back_populates="users")

    def is_admin(self):
        if self.role.name == "admin":
            return True
        else:
            return False
