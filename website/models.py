from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import URLValidator


class HomePageSection(models.Model):
    """CMS model for homepage sections"""
    SECTION_CHOICES = [
        ('hero', 'Hero Section'),
        ('features', 'Features / Why Choose Us'),
        ('services', 'Services Section'),
        ('process', 'Process Section'),
        ('stats', 'Statistics Section'),
        ('portfolio', 'Portfolio Section'),
        ('team', 'Team Section'),
        ('testimonials', 'Testimonials Section'),
        ('consultation', 'Consultation Section'),
        ('faq', 'FAQ Section'),
        ('blog', 'Blog Section'),
        ('contact', 'Contact Section'),
        ('cta', 'Call to Action'),
    ]
    
    section_type = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.TextField(blank=True)
    content = RichTextField(blank=True)
    background_image = models.ImageField(upload_to='website/backgrounds/', blank=True, null=True)
    background_color = models.CharField(max_length=7, default='#0006B1', help_text='Hex color code')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Homepage Section"
        verbose_name_plural = "Homepage Sections"
    
    def __str__(self):
        return self.get_section_type_display()


class Statistic(models.Model):
    """Statistics for homepage"""
    number = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default='fas fa-chart-line', help_text='Font Awesome icon class')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.number} - {self.label}"


class ServicePage(models.Model):
    """CMS model for service pages"""
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.TextField(blank=True)
    hero_background_image = models.ImageField(upload_to='website/services/', blank=True, null=True)
    intro_text = RichTextField(blank=True)
    main_content = RichTextField()
    features_title = models.CharField(max_length=200, blank=True)
    process_title = models.CharField(max_length=200, blank=True)
    cta_title = models.CharField(max_length=200, blank=True)
    cta_text = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Service Pages"
    
    def __str__(self):
        return self.title


class ServiceFeature(models.Model):
    """Features for service pages"""
    service = models.ForeignKey(ServicePage, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-check-circle', help_text='Font Awesome icon class')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class AboutPageContent(models.Model):
    """CMS model for about page"""
    hero_title = models.CharField(max_length=200, default='About Novyra Marketing')
    hero_subtitle = models.TextField(blank=True)
    intro_text = RichTextField()
    mission_title = models.CharField(max_length=200, default='Our Mission')
    mission_text = RichTextField()
    values_title = models.CharField(max_length=200, default='Our Values')
    cta_title = models.CharField(max_length=200, blank=True)
    cta_text = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"
    
    def __str__(self):
        return "About Page Content"
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class AboutValue(models.Model):
    """Values for about page"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-star', help_text='Font Awesome icon class')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class ContactPageContent(models.Model):
    """CMS model for contact page"""
    hero_title = models.CharField(max_length=200, default='Contact Us')
    hero_subtitle = models.TextField(blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    business_hours = models.TextField(blank=True)
    form_title = models.CharField(max_length=200, default='Send Us a Message')
    
    class Meta:
        verbose_name = "Contact Page Content"
        verbose_name_plural = "Contact Page Content"
    
    def __str__(self):
        return "Contact Page Content"
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class FloatingBackground(models.Model):
    """Floating/animating background elements"""
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='website/floating/', blank=True, null=True)
    animation_speed = models.CharField(max_length=20, default='slow', choices=[
        ('slow', 'Slow'),
        ('medium', 'Medium'),
        ('fast', 'Fast'),
    ])
    position = models.CharField(max_length=20, default='center', choices=[
        ('top-left', 'Top Left'),
        ('top-right', 'Top Right'),
        ('bottom-left', 'Bottom Left'),
        ('bottom-right', 'Bottom Right'),
        ('center', 'Center'),
    ])
    opacity = models.FloatField(default=0.1, help_text='0.0 to 1.0')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name


class Feature(models.Model):
    """Features/Why Choose Us items for homepage"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-star', help_text='Font Awesome icon class')
    image = models.ImageField(upload_to='website/features/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Feature"
        verbose_name_plural = "Features"
    
    def __str__(self):
        return self.title


class ProcessStep(models.Model):
    """Process steps for homepage"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-check-circle', help_text='Font Awesome icon class')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Process Step"
        verbose_name_plural = "Process Steps"
    
    def __str__(self):
        return f"{self.order}. {self.title}"


class TeamMember(models.Model):
    """Team members for homepage"""
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='website/team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True, validators=[URLValidator()])
    twitter_url = models.URLField(blank=True, validators=[URLValidator()])
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
    
    def __str__(self):
        return self.name
    
    def get_initials(self):
        """Get initials for avatar"""
        parts = self.name.split()
        if len(parts) >= 2:
            return f"{parts[0][0]}{parts[-1][0]}".upper()
        return self.name[:2].upper()


class Testimonial(models.Model):
    """Testimonials for homepage"""
    client_name = models.CharField(max_length=200)
    client_position = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    testimonial_text = models.TextField()
    client_photo = models.ImageField(upload_to='website/testimonials/', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5, help_text='Rating out of 5')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    
    def __str__(self):
        return f"{self.client_name} - {self.company or 'Testimonial'}"


class ConsultationSection(models.Model):
    """Consultation section for homepage"""
    title = models.CharField(max_length=200, default='Free Consultation')
    subtitle = models.TextField(blank=True)
    description = RichTextField(blank=True)
    button_text = models.CharField(max_length=100, default='Get Started')
    background_image = models.ImageField(upload_to='website/consultation/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Consultation Section"
        verbose_name_plural = "Consultation Section"
    
    def __str__(self):
        return "Consultation Section"
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class FAQ(models.Model):
    """Frequently Asked Questions"""
    question = models.CharField(max_length=500)
    answer = RichTextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
    
    def __str__(self):
        return self.question


class FooterContent(models.Model):
    """Footer content management"""
    about_text = models.TextField(blank=True, help_text='About text in footer')
    copyright_text = models.CharField(max_length=200, default='© 2025 Novyra Marketing LLC. All rights reserved.')
    newsletter_title = models.CharField(max_length=200, blank=True)
    newsletter_text = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Footer Content"
        verbose_name_plural = "Footer Content"
    
    def __str__(self):
        return "Footer Content"
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class NavigationLink(models.Model):
    """Custom navigation links"""
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, help_text='URL path or external URL')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_external = models.BooleanField(default=False, help_text='Check if external URL')
    
    class Meta:
        ordering = ['order']
        verbose_name = "Navigation Link"
        verbose_name_plural = "Navigation Links"
    
    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    phone = models.CharField(max_length=50, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"{self.name} - {self.email} ({self.created_at.strftime('%Y-%m-%d')})"


class VideoSection(models.Model):
    """Video sections for homepage"""
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    video_url = models.URLField(help_text='YouTube or Vimeo URL (will be converted to embed format)')
    thumbnail = models.ImageField(upload_to='website/videos/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Video Section"
        verbose_name_plural = "Video Sections"
    
    def __str__(self):
        return self.title or f"Video {self.id}"
    
    def get_embed_url(self):
        """Convert YouTube/Vimeo URL to embed format"""
        import re
        url = self.video_url
        
        # YouTube URL patterns
        youtube_patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)',
            r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]+)',
            r'(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)',
        ]
        
        for pattern in youtube_patterns:
            match = re.search(pattern, url)
            if match:
                video_id = match.group(1)
                return f'https://www.youtube.com/embed/{video_id}'
        
        # Vimeo URL patterns
        vimeo_patterns = [
            r'(?:https?://)?(?:www\.)?vimeo\.com/(\d+)',
            r'(?:https?://)?(?:www\.)?vimeo\.com/embed/(\d+)',
        ]
        
        for pattern in vimeo_patterns:
            match = re.search(pattern, url)
            if match:
                video_id = match.group(1)
                return f'https://player.vimeo.com/video/{video_id}'
        
        # If already an embed URL, return as is
        if 'embed' in url or 'player.vimeo.com' in url:
            return url
        
        # Return original if no pattern matches
        return url


class PricingPackage(models.Model):
    """Pricing packages for services"""
    name = models.CharField(max_length=100, help_text='e.g., Basic Package, Premium Package, Elite Package')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Price in Nigerian Naira (₦)')
    currency = models.CharField(max_length=10, default='₦', help_text='Currency symbol')
    billing_period = models.CharField(max_length=50, default='month', help_text='e.g., month, year, one-time')
    features = models.JSONField(default=list, help_text='List of features as strings')
    is_featured = models.BooleanField(default=False, help_text='Highlight this package')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'price']
        verbose_name = "Pricing Package"
        verbose_name_plural = "Pricing Packages"
    
    def __str__(self):
        return f"{self.name} - {self.currency}{self.price:,.0f}/{self.billing_period}"
    
    def get_display_price(self):
        """Get formatted price string"""
        return f"{self.currency}{self.price:,.0f}/{self.billing_period}"
