#!/bin/bash
# Build script for Render deployment
# This ensures migrations run before collectstatic

set -e  # Exit on any error

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build complete!"

