from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped


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

    @classmethod
    def get_session(cls):
        with cls.SESSION.begin() as session:
            yield session



from .models import User