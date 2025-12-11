"""
Database initialization script
Run this to set up the database with migrations and initial data
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novyra_cms.settings')
django.setup()

from django.core.management import call_command
from django.db import connection
from django.core.management import execute_from_command_line
import sys

def init_database():
    """Initialize database with migrations"""
    print("=" * 60)
    print("Initializing Database...")
    print("=" * 60)
    
    # Run migrations
    print("\n1. Running migrations...")
    try:
        call_command('migrate', verbosity=1, interactive=False)
        print("[OK] Migrations completed successfully!")
    except Exception as e:
        print(f"[ERROR] Migration error: {e}")
        return False
    
    # Check if SiteSettings exists, create if not
    print("\n2. Initializing SiteSettings...")
    try:
        from settings_app.models import SiteSettings
        settings, created = SiteSettings.objects.get_or_create(pk=1)
        if created:
            print("[OK] SiteSettings created!")
        else:
            print("[OK] SiteSettings already exists!")
    except Exception as e:
        print(f"[WARNING] SiteSettings error (non-critical): {e}")
    
    # Check if superuser exists
    print("\n3. Checking for superuser...")
    try:
        from django.contrib.auth.models import User
        if not User.objects.filter(is_superuser=True).exists():
            print("[INFO] No superuser found. Create one with: python manage.py createsuperuser")
        else:
            print("[OK] Superuser exists!")
    except Exception as e:
        print(f"[WARNING] User check error: {e}")
    
    print("\n" + "=" * 60)
    print("Database initialization complete!")
    print("=" * 60)
    return True

if __name__ == '__main__':
    success = init_database()
    sys.exit(0 if success else 1)

