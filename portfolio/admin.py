from django.contrib import admin
from .models import PortfolioCategory, PortfolioItem, PortfolioImage


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'client_name', 'project_date', 'is_featured', 'views', 'created_at']
    list_filter = ['is_featured', 'created_at', 'categories']
    search_fields = ['title', 'description', 'client_name']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['categories']
    inlines = [PortfolioImageInline]
    date_hierarchy = 'created_at'
    readonly_fields = ['views', 'created_at', 'updated_at']


@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = ['portfolio_item', 'order', 'created_at']
    list_filter = ['portfolio_item', 'created_at']
    ordering = ['portfolio_item', 'order']
