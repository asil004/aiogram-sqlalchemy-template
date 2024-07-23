#!/bin/sh

# Activate the virtual environment
source /root/dates_bot/venv/bin/activate

# Generate alembic migration script
alembic revision --autogenerate -m "makemigrations"

# Apply alembic migrations
alembic upgrade head

# Run your bot
python -m bot
