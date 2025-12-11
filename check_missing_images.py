"""
Check which images are referenced in the database but missing from media folder
"""
import os
import django
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novyra_cms.settings')
django.setup()

from django.conf import settings
from settings_app.models import SiteSettings
from website.models import (
    HomePageSection, ServicePage, TeamMember, Testimonial,
    FloatingBackground, Feature, ProcessStep
)
from blog.models import BlogPost
from portfolio.models import PortfolioItem, PortfolioImage
from accounts.models import UserProfile

def check_image_field(obj, field_name, model_name):
    """Check if an image field has a file that exists"""
    field = getattr(obj, field_name, None)
    if not field:
        return None
    
    try:
        if hasattr(field, 'name') and field.name:
            file_path = os.path.join(settings.MEDIA_ROOT, field.name)
            exists = os.path.exists(file_path)
            return {
                'model': model_name,
                'object': str(obj),
                'field': field_name,
                'path': field.name,
                'url': field.url if hasattr(field, 'url') else None,
                'exists': exists
            }
    except Exception as e:
        return {
            'model': model_name,
            'object': str(obj),
            'field': field_name,
            'error': str(e)
        }
    return None

def check_all_images():
    """Check all images in the database"""
    missing = []
    found = []
    
    print("=" * 60)
    print("Checking Images in Database")
    print("=" * 60)
    
    # Site Settings
    try:
        settings_obj = SiteSettings.load()
        for field_name in ['logo', 'favicon']:
            result = check_image_field(settings_obj, field_name, 'SiteSettings')
            if result:
                if result.get('exists'):
                    found.append(result)
                else:
                    missing.append(result)
    except Exception as e:
        print(f"Error checking SiteSettings: {e}")
    
    # Homepage Sections
    for section in HomePageSection.objects.all():
        result = check_image_field(section, 'background_image', 'HomePageSection')
        if result:
            if result.get('exists'):
                found.append(result)
            else:
                missing.append(result)
    
    # Services
    for service in ServicePage.objects.all():
        result = check_image_field(service, 'hero_background', 'ServicePage')
        if result:
            if result.get('exists'):
                found.append(result)
            else:
                missing.append(result)
    
    # Team Members
    for member in TeamMember.objects.all():
        result = check_image_field(member, 'photo', 'TeamMember')
        if result:
            if result.get('exists'):
                found.append(result)
            else:
                missing.append(result)
    
    # Testimonials
    for testimonial in Testimonial.objects.all():
        result = check_image_field(testimonial, 'client_photo', 'Testimonial')
        if result:
            if result.get('exists'):
                found.append(result)
            else:
                missing.append(result)
    
    # Blog Posts
    for post in BlogPost.objects.all():
        result = check_image_field(post, 'featured_image', 'BlogPost')
        if result:
            if result.get('exists'):
                found.append(result)
            else:
                missing.append(result)
    
    # Portfolio Items
    for item in PortfolioItem.objects.all():
        result = check_image_field(item, 'featured_image', 'PortfolioItem')
        if result:
            if result.get('exists'):
                found.append(result)
            else:
                missing.append(result)
        
        # Portfolio Images
        for img in PortfolioImage.objects.filter(portfolio_item=item):
            result = check_image_field(img, 'image', 'PortfolioImage')
            if result:
                if result.get('exists'):
                    found.append(result)
                else:
                    missing.append(result)
    
    # User Profiles
    for profile in UserProfile.objects.all():
        result = check_image_field(profile, 'avatar', 'UserProfile')
        if result:
            if result.get('exists'):
                found.append(result)
            else:
                missing.append(result)
    
    # Print Results
    print(f"\n✅ Found Images: {len(found)}")
    print(f"❌ Missing Images: {len(missing)}")
    
    if missing:
        print("\n" + "=" * 60)
        print("MISSING IMAGES - Need to Upload:")
        print("=" * 60)
        for item in missing:
            print(f"\n{item['model']}: {item['object']}")
            print(f"  Field: {item['field']}")
            print(f"  Path: {item.get('path', 'N/A')}")
            if item.get('url'):
                print(f"  URL: {item['url']}")
    
    if found:
        print("\n" + "=" * 60)
        print("FOUND IMAGES:")
        print("=" * 60)
        for item in found[:10]:  # Show first 10
            print(f"✅ {item['model']}: {item['object']} - {item['field']}")
        if len(found) > 10:
            print(f"... and {len(found) - 10} more")
    
    return missing, found

if __name__ == '__main__':
    missing, found = check_all_images()
    print(f"\n{'='*60}")
    print(f"Summary: {len(found)} images found, {len(missing)} images missing")
    print(f"{'='*60}")

