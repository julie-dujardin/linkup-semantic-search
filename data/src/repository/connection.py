from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy import text, Connection
from sqlalchemy.orm import Session

from sqlalchemy.engine import URL

from data.src.repository.models import Base


@contextmanager
def connect() -> Connection:
    url = URL.create(
        drivername="postgresql",
        username="vectordb",
        password="vectordb",
        host="127.0.0.1",
        port=5433,
        database="vectordb",
    )

    engine = create_engine(url)

    with Session(engine) as session:
        session.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        session.commit()

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
