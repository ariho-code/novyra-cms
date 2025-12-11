from .models import SiteSettings
from website.models import FloatingBackground, FooterContent, NavigationLink, ContactMessage


def site_settings(request):
    """Context processor to make site settings available in all templates"""
    try:
        settings = SiteSettings.load()
    except:
        settings = None
    
    try:
        floating_bgs = FloatingBackground.objects.filter(is_active=True)
    except:
        floating_bgs = []
    
    try:
        footer_content = FooterContent.load() if FooterContent.objects.exists() else None
    except:
        footer_content = None
    
    try:
        nav_links = NavigationLink.objects.filter(is_active=True)
    except:
        nav_links = []
    
    # Get unread contact messages count for CMS
    unread_messages_count = 0
    if request.user.is_authenticated:
        try:
            unread_messages_count = ContactMessage.objects.filter(is_read=False).count()
        except:
            pass
    
    return {
        'site_settings': settings,
        'floating_backgrounds': floating_bgs,
        'footer_content': footer_content,
        'nav_links': nav_links,
        'unread_messages_count': unread_messages_count,
    }

