run.bot:
	python -m bot

makemigrations:
	alembic revision --autogenerate -m "makemigrations"

migrate:
	alembic upgrade head

