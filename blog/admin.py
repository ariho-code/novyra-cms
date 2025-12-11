from django.contrib import admin
from .models import Category, BlogPost


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at', 'views']
    list_filter = ['status', 'created_at', 'categories']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['categories']
    date_hierarchy = 'created_at'
    readonly_fields = ['views', 'created_at', 'updated_at']
