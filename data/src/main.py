from data.src.embedding import Embedder
from data.src.repository.connection import connect

if __name__ == "__main__":
    embedder = Embedder()
    embedder.embed()

    with connect() as session:
        embedder.save_embeddings(session)
