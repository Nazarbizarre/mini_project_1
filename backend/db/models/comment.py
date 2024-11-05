from sqlalchemy.orm import Mapped, relationship, mapped_column

from .. import Base, PublishedMixin


class Comment(Base, PublishedMixin):
    __tablename__ = "comments"

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="comments")
    content: Mapped[str]
    # author: Author = Field(..., description="The author of the comment")
    # content: Optional[str] = Field(None, description="The content of the comment")
    # created_at: Optional[datetime] = datetime.now
