FROM python:3.12

COPY --from=ghcr.io/astral-sh/uv:0.5.5 /uv /uvx /bin/

ADD /frontend /frontend
WORKDIR /frontend

RUN uv sync --frozen

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["uv", "run", "streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
