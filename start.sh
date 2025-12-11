#!/bin/bash
# Startup script for Render deployment
# Ensures migrations run before starting the server

set -e

echo "=========================================="
echo "Initializing Database..."
echo "=========================================="

# Run migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Initialize SiteSettings if needed
echo "Initializing SiteSettings..."
python -c "
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novyra_cms.settings')
django.setup()
try:
    from settings_app.models import SiteSettings
    settings, created = SiteSettings.objects.get_or_create(pk=1)
    print('[OK] SiteSettings initialized!' if created else '[OK] SiteSettings already exists!')
except Exception as e:
    print('[WARNING] SiteSettings initialization skipped:', str(e))
" || echo "SiteSettings initialization skipped"

echo "=========================================="
echo "Starting application server..."
echo "=========================================="
exec gunicorn novyra_cms.wsgi:application --bind 0.0.0.0:${PORT:-10000} --workers 2 --threads 2 --timeout 120

