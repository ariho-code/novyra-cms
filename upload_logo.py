"""
Script to upload the logo to SiteSettings
Run: python upload_logo.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novyra_cms.settings')
django.setup()

from settings_app.models import SiteSettings
from django.core.files import File

def upload_logo():
    logo_path = 'novyralogo.jpg'
    
    if not os.path.exists(logo_path):
        print(f"❌ Logo file not found: {logo_path}")
        return
    
    settings = SiteSettings.load()
    
    if settings.logo:
        print("⚠️  Logo already exists. Skipping upload.")
        print(f"   Current logo: {settings.logo.url}")
        return
    
    with open(logo_path, 'rb') as f:
        settings.logo.save('logo.jpg', File(f), save=True)
    
    print("✅ Logo uploaded successfully!")
    print(f"   Logo URL: {settings.logo.url}")

if __name__ == '__main__':
    upload_logo()

