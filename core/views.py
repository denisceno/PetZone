from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'core/home-page.html')