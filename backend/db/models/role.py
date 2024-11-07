from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base


class Role(Base):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(unique=True)
    users: Mapped[List["Author"]] = relationship(back_populates="role")
