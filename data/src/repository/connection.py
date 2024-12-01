import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy import text, Connection
from sqlalchemy.orm import Session

from sqlalchemy.engine import URL

from .models import Base


@contextmanager
def connect() -> Connection:
    """
    local dev:
    POSTGRES_DB=vectordb;POSTGRES_HOST=127.0.0.1;POSTGRES_PASSWORD=vectordb;POSTGRES_PORT=5433;POSTGRES_USER=vectordb
    """
    url = URL.create(
        drivername="postgresql",
        username=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host=os.environ["POSTGRES_HOST"],
        port=int(os.environ["POSTGRES_PORT"]),
        database=os.environ["POSTGRES_DB"],
    )

    engine = create_engine(url)

    with Session(engine) as session:
        session.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        session.commit()

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
