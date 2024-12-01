FROM python:3.12

COPY --from=ghcr.io/astral-sh/uv:0.5.5 /uv /uvx /bin/

ADD /data /data
WORKDIR /data

RUN uv sync --frozen

CMD ["uv", "run", "python", "-m", "src.fill_db"]
