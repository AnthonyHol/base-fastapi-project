FROM python:3.11.10-slim

COPY --from=ghcr.io/astral-sh/uv:0.11.16 /uv /uvx /bin/

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UV_PROJECT_ENVIRONMENT=/usr/local
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_LINK_MODE=copy

RUN apt update \
  && apt install -y netcat-traditional make \
  && apt-get install -y curl

COPY ./src/pyproject.toml ./src/uv.lock ./

ARG DEV_DEPS=False

RUN if [ $DEV_DEPS = True ] ; then \
  uv sync --locked --no-install-project ; else \
  uv sync --locked --no-install-project --no-dev ; fi

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY .. .

WORKDIR /usr/src/app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
