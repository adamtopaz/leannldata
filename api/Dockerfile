FROM ubuntu:latest

RUN apt-get update && apt-get install curl git python-is-python3 python3-pip -y

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

COPY main.py main.py

RUN pip install --upgrade pip
RUN pip install --upgrade poetry

RUN poetry config virtualenvs.in-project true
RUN poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
