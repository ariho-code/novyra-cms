"""
Custom error handlers for better error reporting
"""
import traceback
from django.http import HttpResponseServerError
from django.template import loader
from django.conf import settings


def handler500(request):
    """
    Custom 500 error handler that shows the actual error
    """
    template = loader.get_template('500.html')
    context = {}
    
    # In DEBUG mode, try to get the exception info
    if settings.DEBUG:
        import sys
        exc_type, exc_value, exc_traceback = sys.exc_info()
        if exc_type:
            context['error_type'] = str(exc_type.__name__)
            context['error_message'] = str(exc_value)
            context['traceback'] = traceback.format_exception(exc_type, exc_value, exc_traceback)
    
    return HttpResponseServerError(template.render(context, request))

