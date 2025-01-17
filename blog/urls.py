from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:id>/', views.blog_detail, name='blog_detail'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:id>/edit/', views.blog_edit, name='blog_edit'),
    path('<int:id>/delete/', views.blog_delete, name='blog_delete'),
    ]

