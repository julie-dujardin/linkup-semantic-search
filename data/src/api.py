from fastapi import FastAPI
from data.src.repository.connection import connect
from data.src.embedding import Embedder


with connect() as session:
    embedder = Embedder()
    app = FastAPI()


    @app.get("/")
    async def root():
        results = embedder.query_db(session, "accident sportif", 5)
        return [{
            "url": r.url,
            "title": r.title,
            "description": r.description,
            "creator": r.creator,
        } for r in results]
