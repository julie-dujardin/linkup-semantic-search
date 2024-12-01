from fastapi import FastAPI
from .repository.connection import connect
from .embedding import Embedder


with connect() as session:
    embedder = Embedder()
    app = FastAPI()

    @app.get("/")
    async def root(query: str, limit: int = 10):
        results = embedder.query_db(session, query, limit)
        return [
            {
                "url": r.url,
                "title": r.title,
                "description": r.description,
                "creator": r.creator,
                "source": r.source,
                "article": r.article,
                "published_at": r.published_at,
            }
            for r in results
        ]
