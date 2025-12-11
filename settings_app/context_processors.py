from .models import SiteSettings
from website.models import FloatingBackground, FooterContent, NavigationLink, ContactMessage
from django.db import OperationalError, DatabaseError


def site_settings(request):
    """Context processor to make site settings available in all templates"""
    # Initialize defaults
    settings = None
    floating_bgs = []
    footer_content = None
    nav_links = []
    unread_messages_count = 0
    
    # Try to load site settings - handle database errors gracefully
    try:
        settings = SiteSettings.load()
    except (OperationalError, DatabaseError) as e:
        # Database table doesn't exist or connection error
        settings = None
    except Exception as e:
        # Any other error - log but don't crash
        settings = None
    
    # Try to load floating backgrounds
    try:
        floating_bgs = list(FloatingBackground.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        floating_bgs = []
    except Exception:
        floating_bgs = []
    
    # Try to load footer content
    try:
        if FooterContent.objects.exists():
            footer_content = FooterContent.load()
    except (OperationalError, DatabaseError):
        footer_content = None
    except Exception:
        footer_content = None
    
    # Try to load navigation links
    try:
        nav_links = list(NavigationLink.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        nav_links = []
    except Exception:
        nav_links = []
    
    # Get unread contact messages count for CMS
    if request.user.is_authenticated:
        try:
            unread_messages_count = ContactMessage.objects.filter(is_read=False).count()
        except (OperationalError, DatabaseError):
            unread_messages_count = 0
        except Exception:
            unread_messages_count = 0
    
    return {
        'site_settings': settings,
        'floating_backgrounds': floating_bgs,
        'footer_content': footer_content,
        'nav_links': nav_links,
        'unread_messages_count': unread_messages_count,
    }

