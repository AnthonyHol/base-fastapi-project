# Base FastAPI Project
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![uv](https://img.shields.io/badge/uv-%23DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Descriptions
Project with the basic structure of the FastAPI application

## Run
#### Run local environment stack
```shell
docker-compose up -d --build
```

#### Install uv
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Install the project dependencies
```shell
cd src && uv sync
```

#### Run the server within the virtual environment
```shell
uv run uvicorn main:app --reload
```

## Migrations

#### Generate new migration
```shell
alembic revision --autogenerate -m "Migration Name"
```

#### Run migrations
```shell
alembic upgrade head
```

#### Downgrade last migration
```shell
alembic downgrade -1
```

## Development

#### Make lint, tests
```shell
cd src && make lint
cd src && make test
```

#### Branch naming
```
feature/{feature-name-in-kebab-case}  # branch with new functionality, code
fix/{fix-name-in-kebab-case}  # branch with fix changes
```

#### Commit messages
```
+ {message}  # adding new functionality, code
- {message}  # removing functionality, code
! {message}  # changing functionality, code
```
