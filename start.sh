#!/bin/bash
# Startup script for Render deployment
# Ensures migrations run before starting the server

set -e

echo "Running database migrations..."
python manage.py migrate --noinput || echo "Migrations failed, continuing..."

echo "Starting application server..."
exec gunicorn novyra_cms.wsgi:application --bind 0.0.0.0:${PORT:-10000} --workers 2 --threads 2 --timeout 120

