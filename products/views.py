from .models import Products
from django.shortcuts import render ,redirect , get_object_or_404 , HttpResponse
from .forms import Form_Products
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test ,login_required

def superuser_required(view_func):
    return user_passes_test(lambda user: user.is_superuser)(view_func)

# Create your views here.

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
    product = get_object_or_404(Products, id=id)
    context = {
        'product':product
    }
    return render(request,template_name,context)

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



