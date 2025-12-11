from django.db import OperationalError, DatabaseError

# Import models with error handling
try:
    from .models import SiteSettings
    from website.models import FloatingBackground, FooterContent, NavigationLink, ContactMessage
    MODELS_AVAILABLE = True
except Exception:
    MODELS_AVAILABLE = False
    SiteSettings = None
    FloatingBackground = None
    FooterContent = None
    NavigationLink = None
    ContactMessage = None


def site_settings(request):
    """Context processor to make site settings available in all templates"""
    # Wrap entire function in try-except to ensure it NEVER crashes
    try:
        # Initialize defaults - always return safe values
        settings = None
        floating_bgs = []
        footer_content = None
        nav_links = []
        unread_messages_count = 0
        
        # If models aren't available, return defaults immediately
        if not MODELS_AVAILABLE:
            return {
                'site_settings': None,
                'floating_backgrounds': [],
                'footer_content': None,
                'nav_links': [],
                'unread_messages_count': 0,
            }
        
        # Try to load site settings - handle ALL errors gracefully
        try:
            settings = SiteSettings.load()
        except (OperationalError, DatabaseError):
            settings = None
        except Exception:
            settings = None
        
        # Try to load floating backgrounds
        try:
            floating_bgs = list(FloatingBackground.objects.filter(is_active=True))
        except (OperationalError, DatabaseError):
            floating_bgs = []
        except Exception:
            floating_bgs = []
        
        # Try to load footer content - wrap exists() call separately
        try:
            exists = FooterContent.objects.exists()
            if exists:
                footer_content = FooterContent.load()
            else:
                footer_content = None
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
        try:
            if hasattr(request, 'user') and request.user.is_authenticated:
                try:
                    unread_messages_count = ContactMessage.objects.filter(is_read=False).count()
                except (OperationalError, DatabaseError):
                    unread_messages_count = 0
                except Exception:
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
    except Exception:
        # If ANYTHING goes wrong, return safe defaults
        return {
            'site_settings': None,
            'floating_backgrounds': [],
            'footer_content': None,
            'nav_links': [],
            'unread_messages_count': 0,
        }

