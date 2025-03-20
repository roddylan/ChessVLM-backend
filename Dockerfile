FROM python:3.13-slim AS builder

RUN mkdir /cvlmback

WORKDIR /cvlmback

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN pip install --upgrade pip

COPY requirements.txt /cvlmback/

RUN pip install --no-cache-dir -r requirements.txt

# prod
FROM python:3.13-slim

RUN useradd -m -r appuser && \
    mkdir /cvlmback && \
    chown -R appuser /cvlmback

COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin /usr/local/bin/

WORKDIR /cvlmback

COPY --chown=appuser:appuser . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER appuser

EXPOSE 8000


# COPY . /cvlmback/

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "chessvlmbackend.asgi", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]
