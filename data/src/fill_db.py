from .embedding import Embedder
from .repository.connection import connect

if __name__ == "__main__":
    embedder = Embedder()
    embedder.embed()

    with connect() as session:
        embedder.save_embeddings(session)
