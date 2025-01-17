from django.shortcuts import render, redirect
from products.models import Products
from .forms import AppointmentForm
from django.http import HttpResponse
from .models import Appointment
import smtplib

import os
from dotenv import load_dotenv

load_dotenv()

email_txt = "Thank you for scheduling an appointment with us!"
my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('MY_PASSWORD')


def email_s(user_email, email_txt):
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=user_email,
                msg=f"Subject:Appointment Confirmation\n\n{email_txt}"
            )
    except Exception as e:
        print(f"Error sending email: {e}")


def appointment_home(request):
    template_name = "appointments/appointments-home.html"
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            email_s(appointment.email, email_txt)
            return redirect("home-page")
    else:
        form = AppointmentForm()

    context = {
        "form": form,
    }
    return render(request, template_name, context)

def appointment_list(request):
    template_name = 'appointments/appointment_list.html'
    appointments = Appointment.objects.all().order_by('-appointment_date')
    context = {
        'appointments': appointments
    }
    return render(request, template_name, context)