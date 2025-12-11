"""
URL configuration for novyra_cms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import init_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Public website
    path("", include("website.urls")),
    # CMS Dashboard (admin area)
    path("cms/", views.dashboard, name="dashboard"),
    path("cms/dashboard/", views.dashboard, name="dashboard"),
    path("cms/blog/", include("blog.urls")),
    path("cms/portfolio/", include("portfolio.urls")),
    path("cms/accounts/", include("accounts.urls")),
    path("cms/settings/", include("settings_app.urls")),
    # Website Content Management
    path("cms/website/", include("website.cms_urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    # Initialization endpoints (for Render free tier)
    path("init-database/", init_views.init_database, name="init_database"),
    path("create-admin/", init_views.create_admin, name="create_admin"),
    path("check-database/", init_views.check_database, name="check_database"),
    path("import-data/", init_views.import_data, name="import_data"),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # In production, you should serve media files through your web server
    # For now, we'll serve them here too for testing
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
