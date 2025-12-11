from django import template
from django.core.files.images import ImageFile

register = template.Library()


@register.filter
def has_file(field):
    """Check if an ImageField/FileField has an actual file"""
    if not field:
        return False
    try:
        # Check if the field has a name attribute and it's not empty
        # This indicates a file has been uploaded
        if hasattr(field, 'name') and field.name:
            # Try to access url - this will raise ValueError if no file is associated
            try:
                url = field.url
                return bool(url)  # Return True if URL exists
            except (ValueError, AttributeError):
                return False
        return False
    except (AttributeError, TypeError):
        return False

