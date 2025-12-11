from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SiteSettings
from .forms import SiteSettingsForm


@login_required
def settings_view(request):
    settings = SiteSettings.load()
    
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
