from django.urls import path
from . import views, cms_views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('create/', views.blog_create, name='create'),
    # CMS Category Management - Must come before slug patterns
    path('categories/', cms_views.cms_categories, name='categories'),
    path('categories/create/', cms_views.cms_category_create, name='category_create'),
    path('categories/<int:pk>/update/', cms_views.cms_category_update, name='category_update'),
    path('categories/<int:pk>/delete/', cms_views.cms_category_delete, name='category_delete'),
    path('categories/<int:pk>/get/', cms_views.cms_category_get, name='category_get'),
    # Blog post URLs - Must come after categories
    path('<slug:slug>/', views.blog_detail, name='detail'),
    path('<slug:slug>/edit/', views.blog_edit, name='edit'),
    path('<slug:slug>/delete/', views.blog_delete, name='delete'),
]

