"""
Quick script to create a superuser non-interactively
Run: python create_superuser.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novyra_cms.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser if it doesn't exist
username = 'admin'
email = 'admin@novyra.com'
password = 'admin123'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'✅ Superuser created successfully!')
    print(f'   Username: {username}')
    print(f'   Password: {password}')
else:
    print(f'⚠️  User "{username}" already exists!')

