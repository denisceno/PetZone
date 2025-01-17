from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.custom_register, name='register'),
    path('login_user/', views.custom_login, name='login'),
    path('logout_user/', views.custom_logout, name='logout'),
]
