from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Settings', {
            'fields': ('site_title', 'tagline', 'site_description', 'admin_email', 'logo', 'favicon')
        }),
        ('Location Information', {
            'fields': ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'phone')
        }),
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url')
        }),
        ('Security Settings', {
            'fields': ('two_factor_enabled', 'login_attempts_limit', 'session_timeout')
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
