from sqlalchemy import Column, Integer, DateTime, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column

from pgvector.sqlalchemy import Vector


Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer(), primary_key=True)
    source = Column(Text())
    title = Column(Text())
    description = Column(Text())
    article = Column(Text())
    url = Column(Text())
    creator = Column(Text())
    published_at = Column(DateTime())

    embedding = mapped_column(Vector())

    def __repr__(self) -> str:
        return self.title
