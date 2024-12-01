# Semantic Search Technical Test

Pull news articles from the web, and run semantic search queries against them

See the full requirements at [semantic_search.pdf](https://github.com/julie-dujardin/linkup-semantic-search/blob/93af30767d59a823d01878f15b19814c10f5f4d7/semantic_search.pdf)

## Run the project

```shell
cd deploy
docker-compose up
```

open `http://127.0.0.1:8501/`
## How it works

1. Pull 50 articles from both vsd.fr and public.fr, using their RSS feeds,
2. compute the embeddings of those articles using sentence_transformers,
3. store the embeddings and some basic article data to the pgvector database. This makes it trivial to query using the embeddings, and retrieve all associated data.
4. When the backend receives a query, compute its embeddings & query that to the database,
5. expose the results with a simple FastAPI service.
6. The frontend is a super basic streamlit app.

## Notes

The project was completed in about 4.5 hours. This was a big learning experience for me, I'd never used sentence_transformers, pgvector, sqlAlchemy, fastAPI (almost never), or streamlit before.

### Future improvements

The project structure definitely needs improvement: fill_db and the api should be split into 2 modules with some common files.

The API needs a big rework to use SQLModel, which I didn't know you were supposed to use with FastAPI. My dirty hack to use sqlAlchemy works, but I am ashamed of it. This will also make it easy to use proper serialization.

Right now, the database only contains the last 50 articles from each RSS feed. Articles that are already in the DB should be left in there, and new articles should be added. We also need a way to retrieve older articles. For example, through the [wayback machine](http://web.archive.org/web/20240723150148/https://www.public.fr/feed) or some other archive.

The dockerfiles are also an easy improvement: the venv should be built before including the source code, so we're not rebuilding the entire env every time the code is changed. This would significantly reduce build times.

To make the app testable, we need to add a local only mode, where we're pulling from a local dataset instead of hitting up the real RSS feeds. This would also prevent us from hitting rate limits. Once this is done, we can add a CI that runs tests & ruff.

Finally, a proper web server should be standing in front of the app to make it production ready.

### DB

I'm pretty happy with the choice of pgvector, it gives us the power of postgreSQL (scalability, low cost, everything in one place, easy operations), with some drawbacks (I imagine there's some missing LLM stuff that a fully dedicated LLM database would have?).
