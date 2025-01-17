from django.urls import path
from . import views


urlpatterns = [
    path('apointment/',views.appointment_home,name='appointment-home'),
    path('appointment_list/',views.appointment_list,name='appointment-list'),
]