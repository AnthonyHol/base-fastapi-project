FROM python:3.11.10-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
  && apt install -y netcat-traditional make \
  && pip install --upgrade pip \
  && pip install poetry \
  && apt-get install -y curl

COPY ./src/pyproject.toml ./src/poetry.lock ./

ARG DEV_DEPS=False

RUN poetry config virtualenvs.create false
RUN if [ $DEV_DEPS = True ] ; then \
  poetry install --no-interaction --no-ansi ; else \
  poetry install --only main --no-interaction --no-ansi ; fi

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY .. .

WORKDIR /usr/src/app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]