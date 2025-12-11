from django.contrib import admin
from .models import (
    HomePageSection, Statistic, ServicePage, ServiceFeature,
    AboutPageContent, AboutValue, ContactPageContent, FloatingBackground,
    Feature, ProcessStep, TeamMember, Testimonial, ConsultationSection,
    FAQ, FooterContent, NavigationLink, ContactMessage, VideoSection,
    PricingPackage
)


@admin.register(HomePageSection)
class HomePageSectionAdmin(admin.ModelAdmin):
    list_display = ['section_type', 'title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['section_type', 'is_active']


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['number', 'label', 'is_active', 'order']
    list_editable = ['is_active', 'order']


class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1


@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('slug', 'title', 'is_active')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_background_image')
        }),
        ('Content', {
            'fields': ('intro_text', 'main_content')
        }),
        ('Sections', {
            'fields': ('features_title', 'process_title', 'cta_title', 'cta_text')
        }),
    )


@admin.register(AboutPageContent)
class AboutPageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not AboutPageContent.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AboutValue)
class AboutValueAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order']
    list_editable = ['is_active', 'order']


@admin.register(ContactPageContent)
class ContactPageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ContactPageContent.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FloatingBackground)
class FloatingBackgroundAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'animation_speed', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active', 'position', 'animation_speed']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'position']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'company', 'rating', 'is_active', 'order']
    list_editable = ['is_active', 'order', 'rating']
    list_filter = ['is_active', 'rating']
    search_fields = ['client_name', 'company']


@admin.register(ConsultationSection)
class ConsultationSectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ConsultationSection.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['question', 'answer']


@admin.register(FooterContent)
class FooterContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not FooterContent.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'is_external', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active', 'is_external']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'phone', 'created_at']
    list_editable = ['is_read']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Message Information', {
            'fields': ('name', 'email', 'phone', 'subject', 'message', 'is_read', 'created_at')
        }),
    )
    
    def has_add_permission(self, request):
        return False


@admin.register(VideoSection)
class VideoSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']


@admin.register(PricingPackage)
class PricingPackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_display_price', 'is_featured', 'is_active', 'order']
    list_editable = ['is_featured', 'is_active', 'order']
    list_filter = ['is_active', 'is_featured']
    search_fields = ['name']
    ordering = ['order', 'price']
