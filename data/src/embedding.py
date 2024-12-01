import torch

from sentence_transformers import SentenceTransformer

from repository.models import Article
from rss import RssParser


class Embedder:
    def __init__(self):
        self.embedder = SentenceTransformer("distiluse-base-multilingual-cased-v1")
        self.articles = []
        self.embeddings = []

    def embed(self):
        self.articles = RssParser.get_all()
        corpus = [a["article"] for a in self.articles]
        self.embeddings = self.embedder.encode(corpus, convert_to_tensor=True)

    def save_embeddings(self, session):
        db_articles = []

        for i, article in enumerate(self.articles):
            db_articles.append(
                Article(
                    source=article["source"],
                    title=article["title"],
                    description=article["description"],
                    article=article["article"],
                    url=article["url"],
                    creator=article["creator"],
                    published_at=article["published_at"],
                    embedding=self.embeddings[i].cpu(),
                )
            )

        session.bulk_save_objects(db_articles)
        session.commit()

    def query_corpus(self, query: str) -> list:
        top_k = min(5, len(self.articles))

        query_embedding = self.embedder.encode(query, convert_to_tensor=True)

        # We use cosine-similarity and torch.topk to find the highest 5 scores
        similarity_scores = self.embedder.similarity(query_embedding, self.embeddings)[0]
        scores, indices = torch.topk(similarity_scores, k=top_k)

        return [{"score": score, "article": self.articles[idx]} for score, idx in zip(scores, indices)]
