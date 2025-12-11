from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_list, name='list'),
    path('create/', views.portfolio_create, name='create'),
    path('<slug:slug>/', views.portfolio_detail, name='detail'),
    path('<slug:slug>/edit/', views.portfolio_edit, name='edit'),
    path('<slug:slug>/delete/', views.portfolio_delete, name='delete'),
]

