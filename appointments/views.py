from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from django.contrib import messages
import smtplib

import os
from dotenv import load_dotenv

load_dotenv()


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


from django.contrib import messages  # Import messages framework

def appointment_home(request):
    template_name = "appointments/appointments-home.html"

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            
            appointment = form.save()
            messages.success(request, "Your appointment has been scheduled successfully!")  # Add success message
            name = form.cleaned_data.get('name')
            date = form.cleaned_data.get('appointment_date')
            email_txt = f"Thank you {name} for scheduling an appointment with us! \n\nYour appointment is scheduled for {date}. \n\nWe look forward to seeing you soon!"
            email_s(appointment.email, email_txt)
            return redirect("home-page")  # Redirect to prevent form resubmission
    else:
        form = AppointmentForm()

    return render(request, template_name, {"form": form})


def appointment_list(request):
    template_name = 'appointments/appointment_list.html'
    appointments = Appointment.objects.all().order_by('-appointment_date')
    context = {
        'appointments': appointments
    }
    return render(request, template_name, context)