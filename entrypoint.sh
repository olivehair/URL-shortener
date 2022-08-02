#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Create admin
echo "Create admin"
python manage.py createsuperuser --no-input

# Start server
echo "Starting server"
gunicorn djangoProject1.asgi:application -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
