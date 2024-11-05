from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base, PublishedMixin


class Article(Base, PublishedMixin):
    __tablename__ = "articles"
    title: Mapped[str]
    content: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="articles")
    tags: Mapped[list] = None


# title: str = Field()
#     content: str = Field()
#     author: Author = Field()
#     tags: Optional[list] = None
#     published_at: Optional[datetime] = datetime.now
