.PHONY: help run lint lint-fix test docker-up docker-down docker-build docker-logs

help:
	@echo "Targets:"
	@echo "  run           Run the application"
	@echo "  lint          Check code style with ruff"
	@echo "  lint-fix      Auto-fix lint issues with ruff"
	@echo "  test          Run the test suite with pytest"
	@echo "  docker-up     Start the docker compose stack (postgres, localstack)"
	@echo "  docker-down   Stop the docker compose stack"
	@echo "  docker-build  Build/rebuild the docker compose stack"
	@echo "  docker-logs   Tail logs from the docker compose stack"

run:
	uv run python main.py

lint:
	uv run ruff check .

lint-fix:
	uv run ruff check --fix .

test:
	uv run pytest

docker-up:
	docker compose up -d

docker-down:
	docker compose down

docker-build:
	docker compose up -d --build

docker-logs:
	docker compose logs -f
