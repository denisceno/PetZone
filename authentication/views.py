from django.forms import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . forms import UserRegistrationForm

# Create your views here.

def custom_register(request):
    template_name = 'authentication/register.html'

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Hi <b>{user.username}</b>!, Your account is created successfully and now you are logged in!')
            return redirect('home-page')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    context = { 'form': form }
    return render(request, template_name, context)


def custom_login(request):
    template_name = 'authentication/login.html'

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in successfully...")
                return redirect('home-page')

    else:
        form = AuthenticationForm()

    context = {"form": form}

    return render(request, template_name, context)



def custom_logout(request):
    template_name = 'authentication/logout.html'
    logout(request)
    messages.info(request, "Logged out successfully!")

    return render(request, template_name)


