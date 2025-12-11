from django import forms
from .models import SiteSettings


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = [
            'site_title', 'tagline', 'site_description', 'admin_email',
            'meta_title', 'meta_description', 'meta_keywords',
            'facebook_handle', 'x_handle', 'instagram_handle', 'linkedin_handle',
            'tiktok_handle', 'youtube_handle',
            'two_factor_enabled', 'login_attempts_limit', 'session_timeout',
        ]
        widgets = {
            'site_title': forms.TextInput(attrs={'class': 'form-control'}),
            'tagline': forms.TextInput(attrs={'class': 'form-control'}),
            'site_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'admin_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_handle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., novyramarketing'}),
            'x_handle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., novyramarketing'}),
            'instagram_handle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., novyramarketing'}),
            'linkedin_handle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., company/novyramarketing'}),
            'tiktok_handle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., novyramarketing'}),
            'youtube_handle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., @novyramarketing'}),
            'two_factor_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'login_attempts_limit': forms.NumberInput(attrs={'class': 'form-control'}),
            'session_timeout': forms.NumberInput(attrs={'class': 'form-control'}),
        }

