from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import OperationalError, DatabaseError
from .models import SiteSettings
from .forms import SiteSettingsForm


@login_required
def settings_view(request):
    try:
        settings = SiteSettings.load()
    except (OperationalError, DatabaseError):
        # If database doesn't exist, create a new instance
        settings = SiteSettings()
        settings.pk = 1
    except Exception:
        settings = SiteSettings()
        settings.pk = 1
    
    if request.method == 'POST':
        form = SiteSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully!')
            return redirect('settings:view')
    else:
        form = SiteSettingsForm(instance=settings)
    
    # Get active tab from query parameter
    active_tab = request.GET.get('tab', 'general')
    
    return render(request, 'settings/view.html', {
        'form': form,
        'settings': settings,
        'active_tab': active_tab,
    })
