alembic_cmd:=poetry run alembic --config="backend/infrastructure/postgresql/alembic.ini"

backend.dev:
	poetry run gunicorn 'backend.infrastructure.entrypoints.api:create_app()' \
	--workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000

backend.lint:
	@echo "----------------------------"
	poetry run ruff check --fix backend
	@echo "----------------------------"
	poetry run black backend
	@echo "----------------------------"
	poetry run mypy backend

backend.sql.autogen:
	$(alembic_cmd) \
	revision -m ${message} --autogenerate
