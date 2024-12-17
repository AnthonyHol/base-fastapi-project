# usage: make {command}
# example: make lint
lint:
	@echo "Lint project"
	poetry run ruff format . --check
	poetry run ruff check
	poetry run mypy . --explicit-package-bases

fix:
	@echo "Fix project"
	poetry run ruff format .
	poetry run ruff check . --fix

test:
	@echo "Run tests for Project"
	poetry run pytest