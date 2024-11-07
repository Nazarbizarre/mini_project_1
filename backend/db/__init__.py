from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped


class PublishedMixin:
    published_at: Mapped[datetime] = mapped_column(default=datetime.now())


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class AsyncDB:
    ENGINE = create_engine("sqlite:///users.db")
    SESSION = sessionmaker(bind=ENGINE)

    @classmethod
    def up(cls):
        Base.metadata.create_all(cls.ENGINE)

    @classmethod
    def down(cls):
        Base.metadata.drop_all(cls.ENGINE)

    @classmethod
    def migrate(cls):
        Base.metadata.drop_all(cls.ENGINE)
        Base.metadata.create_all(cls.ENGINE)
        with cls.SESSION.begin() as session:
            admin_role = Role(name="admin")
            user_role = Role(name="default_user")
            session.add(admin_role)
            session.add(user_role)

    @classmethod
    def get_session(cls):
        with cls.SESSION.begin() as session:
            yield session


from .models import Author, Article, Comment, Role
