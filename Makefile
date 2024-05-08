run.bot:
	python -m bot

migrate:
	alembic revision --autogenerate -m "makemigrations"
	alembic upgrade head
