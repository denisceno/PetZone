from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'appointment_date']
        widgets = {
            'appointment_date': forms.TextInput(attrs={'id': 'appointment-date'}),
        }
