FROM python:3.11-slim

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

ENV POETRY_HOME /opt/poetry

RUN python3 -m venv $POETRY_HOME

RUN $POETRY_HOME/bin/pip install poetry==1.5.1

ENV POETRY_BIN $POETRY_HOME/bin/poetry

COPY pyproject.toml poetry.lock ./

RUN $POETRY_BIN config --local virtualenvs.create false

ENV PATH "$POETRY_HOME/bin:$PATH"

RUN $POETRY_BIN install --no-root

COPY . /app

ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV DATABASE_URI=sqlite:///db.sqlite3
ENV SECRET_KEY=My_favorite_micro-framework_is_FLASK!
ENV BASIC_AUTH_USERNAME=microchel
ENV BASIC_AUTH_PASSWORD=microchel007

CMD sh -c "flask run --host=0.0.0.0 & uvicorn server:fastapp --host=0.0.0.0 --port=8000"