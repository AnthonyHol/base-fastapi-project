# usage: make {command}
# example: make lint
lint:
	@echo "Lint project"
	uv run ruff format . ../tests --check
	uv run ruff check . ../tests
	uv run mypy . ../tests --explicit-package-bases
	uv run bandit -c pyproject.toml -r . -x ./.venv

fix:
	@echo "Fix project"
	uv run ruff format . ../tests
	uv run ruff check . ../tests --fix

test:
	@echo "Run tests for Project"
	uv run pytest ../tests