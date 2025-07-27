# prod
FROM python:3.12-slim
RUN apt-get update && apt-get install -y curl
COPY --from=ghcr.io/astral-sh/uv:0.8.3 /uv /uvx /bin/

WORKDIR /cvlmback
COPY . /cvlmback
RUN uv sync --locked

CMD ["uv", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "app.main:app"]