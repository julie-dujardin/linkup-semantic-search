from .embedding import Embedder
from .repository.connection import connect

import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout,
)

if __name__ == "__main__":
    embedder = Embedder()
    logging.info("Pulling data & preparing embeddings")
    embedder.embed()

    with connect() as session:
        logging.info("saving to DB")
        embedder.save_embeddings(session)

    logging.info("update finished")
