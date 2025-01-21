from django.shortcuts import render
from products.models import Products

# Create your views here.

def home_page(request):
    template_name = 'core/home-page.html'
    products = Products.objects.all
    context = {
        'products':products
    }
    return render(request,template_name,context)

def about_us(request):
    template_name = 'core/about-us.html'
    return render(request,template_name)