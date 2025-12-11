"""
Initialize pricing packages from the provided image
"""
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novyra_cms.settings')
django.setup()

from website.models import PricingPackage

def initialize_pricing():
    print("Initializing pricing packages...")
    
    # Clear existing packages (optional - comment out if you want to keep existing)
    # PricingPackage.objects.all().delete()
    
    packages_data = [
        {
            'name': 'Basic Package',
            'price': 30000,
            'currency': '₦',
            'billing_period': 'month',
            'features': [
                'SOCIAL MEDIA ACCOUNT SETUP (UP TO 3 PLATFORMS)',
                '3 BRANDED POSTS/MONTH (GRAPHICS + CAPTIONS)',
                'AD ACCOUNT SETUP (FACEBOOK/INSTAGRAM)',
                'BASIC PAGE SET-UP (BIO, HIGHLIGHTS, CTA BUTTON)',
                '1 PROMOTIONAL VIDEO'
            ],
            'is_featured': False,
            'is_active': True,
            'order': 1
        },
        {
            'name': 'Premium Package',
            'price': 45000,
            'currency': '₦',
            'billing_period': 'month',
            'features': [
                'SOCIAL MEDIA ACCOUNT SETUP (UP TO 3 PLATFORMS)',
                '6 BRANDED POSTS/MONTH (GRAPHICS + CAPTIONS)',
                'AD ACCOUNT SETUP (FACEBOOK/INSTAGRAM)',
                'BASIC PAGE SET-UP (BIO, HIGHLIGHTS, CTA BUTTON)',
                'WEEKLY PERFORMANCE CHECK-IN',
                '3 PROMOTIONAL VIDEOS'
            ],
            'is_featured': True,
            'is_active': True,
            'order': 2
        },
        {
            'name': 'Elite Package',
            'price': 65000,
            'currency': '₦',
            'billing_period': 'month',
            'features': [
                'SOCIAL MEDIA ACCOUNT SETUP (UP TO 3 PLATFORMS)',
                '8 BRANDED POSTS/MONTH (GRAPHICS + CAPTIONS)',
                '2 AD ACCOUNT SETUP (FACEBOOK/INSTAGRAM)',
                'BASIC PAGE SET-UP (BIO, HIGHLIGHTS, CTA BUTTON)',
                'WEEKLY PERFORMANCE CHECK-IN',
                '5 PROMOTIONAL VIDEOS',
                'FULL SOCIAL MEDIA MANAGEMENT'
            ],
            'is_featured': False,
            'is_active': True,
            'order': 3
        }
    ]
    
    for pkg_data in packages_data:
        package, created = PricingPackage.objects.get_or_create(
            name=pkg_data['name'],
            defaults=pkg_data
        )
        if created:
            print(f"[OK] Created {pkg_data['name']}")
        else:
            # Update existing package
            for key, value in pkg_data.items():
                setattr(package, key, value)
            package.save()
            print(f"[OK] Updated {pkg_data['name']}")
    
    print("\n[SUCCESS] Pricing packages initialized successfully!")
    print("\nPackages created:")
    for pkg in PricingPackage.objects.all().order_by('order'):
        print(f"  - {pkg.name}: {pkg.get_display_price()}")

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    initialize_pricing()

