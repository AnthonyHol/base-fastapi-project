# usage: make {command}
# example: make lint
lint:
	@echo "Lint project"
	uv run ruff format . --check
	uv run ruff check
	uv run mypy . --explicit-package-bases
	uv run bandit -c pyproject.toml -r . -x ./.venv

fix:
	@echo "Fix project"
	uv run ruff format .
	uv run ruff check . --fix

test:
	@echo "Run tests for Project"
	uv run pytest