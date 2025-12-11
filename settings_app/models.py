from django.db import models
from django.core.validators import URLValidator


class SiteSettings(models.Model):
    """Singleton model for site-wide settings"""
    site_title = models.CharField(max_length=200, default='Novyra Marketing')
    tagline = models.CharField(max_length=200, default='Digital Marketing Agency')
    site_description = models.TextField(
        default='We help businesses grow through strategic digital marketing, compelling branding, and results-driven campaigns.'
    )
    admin_email = models.EmailField(default='novyramarketingagency@gmail.com')
    logo = models.ImageField(upload_to='site/logo/', blank=True, null=True, help_text='Main site logo')
    favicon = models.ImageField(upload_to='site/favicon/', blank=True, null=True, help_text='Favicon for browser tab')
    
    # Location Information
    address_line_1 = models.CharField(max_length=200, blank=True, default='Lagos, Nigeria')
    address_line_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, default='Lagos')
    state = models.CharField(max_length=100, default='Lagos State')
    country = models.CharField(max_length=100, default='Nigeria')
    phone = models.CharField(max_length=50, blank=True)
    
    # SEO Settings
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=500, blank=True)
    
    # Social Media Handles (just the handle, not full URL)
    facebook_handle = models.CharField(max_length=100, blank=True, help_text='Facebook handle (e.g., novyramarketing)')
    x_handle = models.CharField(max_length=100, blank=True, help_text='X (Twitter) handle without @ (e.g., novyramarketing)')
    instagram_handle = models.CharField(max_length=100, blank=True, help_text='Instagram handle (e.g., novyramarketing)')
    linkedin_handle = models.CharField(max_length=100, blank=True, help_text='LinkedIn handle (e.g., company/novyramarketing)')
    tiktok_handle = models.CharField(max_length=100, blank=True, help_text='TikTok handle (e.g., novyramarketing)')
    youtube_handle = models.CharField(max_length=100, blank=True, help_text='YouTube handle (e.g., @novyramarketing or channel ID)')
    
    # Legacy fields for backward compatibility (deprecated)
    facebook_url = models.URLField(blank=True, validators=[URLValidator()])
    twitter_url = models.URLField(blank=True, validators=[URLValidator()], help_text='Deprecated: Use x_handle instead')
    instagram_url = models.URLField(blank=True, validators=[URLValidator()])
    linkedin_url = models.URLField(blank=True, validators=[URLValidator()])
    tiktok_url = models.URLField(blank=True, validators=[URLValidator()])
    youtube_url = models.URLField(blank=True, validators=[URLValidator()])
    
    # Security Settings
    two_factor_enabled = models.BooleanField(default=False)
    login_attempts_limit = models.PositiveIntegerField(default=5)
    session_timeout = models.PositiveIntegerField(default=60, help_text="Session timeout in minutes")
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    def get_facebook_url(self):
        """Get Facebook URL from handle"""
        if self.facebook_handle:
            return f"https://facebook.com/{self.facebook_handle.lstrip('@/')}"
        return self.facebook_url or ""
    
    def get_x_url(self):
        """Get X (Twitter) URL from handle"""
        if self.x_handle:
            return f"https://x.com/{self.x_handle.lstrip('@/')}"
        return self.twitter_url or ""
    
    def get_instagram_url(self):
        """Get Instagram URL from handle"""
        if self.instagram_handle:
            return f"https://instagram.com/{self.instagram_handle.lstrip('@/')}"
        return self.instagram_url or ""
    
    def get_linkedin_url(self):
        """Get LinkedIn URL from handle"""
        if self.linkedin_handle:
            handle = self.linkedin_handle.lstrip('@/')
            if handle.startswith('company/'):
                return f"https://linkedin.com/{handle}"
            return f"https://linkedin.com/company/{handle}"
        return self.linkedin_url or ""
    
    def get_tiktok_url(self):
        """Get TikTok URL from handle"""
        if self.tiktok_handle:
            return f"https://tiktok.com/@{self.tiktok_handle.lstrip('@/')}"
        return self.tiktok_url or ""
    
    def get_youtube_url(self):
        """Get YouTube URL from handle"""
        if self.youtube_handle:
            handle = self.youtube_handle.lstrip('@/')
            if handle.startswith('@'):
                return f"https://youtube.com/{handle}"
            elif handle.startswith('channel/'):
                return f"https://youtube.com/{handle}"
            else:
                return f"https://youtube.com/@{handle}"
        return self.youtube_url or ""
