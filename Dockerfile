FROM python:3.13.1

RUN mkdir /cvlmback

WORKDIR /cvlmback

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1


RUN pip install --upgrade pip

COPY requirements.txt /cvlmback/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /cvlmback/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

