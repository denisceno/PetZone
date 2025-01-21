from .models import Products , Orders
from django.shortcuts import render ,redirect , get_object_or_404 , HttpResponse
from .forms import Form_Products , Form_Orders
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test ,login_required
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

def superuser_required(view_func):
    return user_passes_test(lambda user: user.is_superuser)(view_func)

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('MY_PASSWORD')


def email_s(user_email, user_name, phone_number):
    email_txt = f"Thank you for your order!\nOur team will contact you soon at the phone number: {phone_number}."
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=user_email,
                msg=f"Subject: Appointment Confirmation\n\nHello {user_name},\n\n{email_txt}"
            )
    except Exception as e:
        print(f"Error sending email: {e}")

#------------------ANIMAL SELECT------------------#

def calculator_home(request):
    template_name = "products/products-home.html"
    return render(request, template_name)

def cat(request):
    template_name = "products/cat.html"
    return render(request, template_name)

def dog(request):
    template_name = "products/dog.html"
    return render(request, template_name)

def cat_age_view(request, age_category):
    if age_category == "over":
        template_name = "products/cat-age-over.html"
    elif age_category == "under":
        template_name = "products/cat-age-under.html"
    else:
        return HttpResponse("Invalid age category", status=400)

    products = Products.objects.filter(
        animal_type__animal_type="Cat",
        age_category__age_category="Over 1" if age_category == "over" else "Under 1"
    )

    context = {
        "products": products,
    }

    return render(request, template_name, context)

def dog_age_view(request, age_category):
    if age_category == "over":
        template_name = "products/dog-age-over.html"
    elif age_category == "under":
        template_name = "products/dog-age-under.html"
    else:
        return HttpResponse("Invalid age category", status=400)

    products = Products.objects.filter(
        animal_type__animal_type="Dog",
        age_category__age_category="Over 1" if age_category == "over" else "Under 1"
    )

    context = {
        "products": products,
    }

    return render(request, template_name, context)


#------------------ALL PRODUCTS------------------#

def all_products(request):
    template_name = 'products/all-products.html'
    products = Products.objects.all
    context = {
        'products':products
    }
    return render(request,template_name,context)


#------------------DESCRIPTION------------------#

def products_detail(request, id):
    template_name = 'products/products-detail.html'
    product = Products.objects.get(id=id) 
    form_orders = Form_Orders()

    if request.method == 'POST':
        form_orders = Form_Orders(request.POST) 
        if form_orders.is_valid():
            order = form_orders.save(commit=False)  
            order.product = product  
            order.save() 
            email_s(order.email, order.name, order.phone)
            return redirect('success_page', order_id=order.id)
    context = {
        'product': product,
        'form_orders': form_orders,
    }
    return render(request, template_name, context)

def success_page(request, order_id):
    order = get_object_or_404(Orders, id=order_id)

    context = {
        'name': order.name, 
        'phone': order.phone,  
    }

    return render(request, 'products/success-page.html', context)

#------------------CREATE------------------#

@login_required
@superuser_required
def create_products(request):
    template_name = 'products/products-create.html'
    if request.method == 'POST':
        form = Form_Products(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('products-home') 
    else:
        form = Form_Products()

    return render(request, template_name, {'form': form})

#------------------UPDATE------------------#

@login_required
@superuser_required
def update_products(request, id):
    template_name = 'products/products-update.html'
    product = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        form = Form_Products(request.POST, request.FILES, instance=product)
        if form.is_valid():
            with transaction.atomic():
                if 'image' in request.FILES:
                    product.image = request.FILES['image']
                form.save()
            return redirect('products-home')
    else:
        form = Form_Products(instance=product)

    context = {
        'form': form,
        'product': product
    }
    
    return render(request, template_name,context)

#------------------DELETE------------------#

@login_required
@superuser_required
def delete_products(request, id):
    template_name = 'products/products-delete.html'
    product = get_object_or_404(Products, id=id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('products-home')
    
    return render(request, template_name, {'product': product})



#------------------Orders------------------#

def orders(request):
    template_name = 'products/orders.html'
    orders = Orders.objects.all().order_by('-order_date')
    context = {
        'orders': orders
    }
    return render(request, template_name, context)