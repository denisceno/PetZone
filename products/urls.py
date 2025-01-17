from django.urls import path
from . import views


urlpatterns = [
    path('',views.calculator_home,name='products-home'),
    
    path('cat/',views.cat,name='cat'),
    path('dog/',views.dog,name='dog'),

    path('cat-age/<str:age_category>/', views.cat_age_view, name='cat_age_view'),
    path('dog-age/<str:age_category>/', views.dog_age_view, name='dog_age_view'),

    path('all-products/',views.all_products,name='all-products'),
    path('products/detail/<uuid:id>/',views.products_detail,name='products-detail'),
    path('products/create/',views.create_products,name='create-product'),
    path('products/update/<uuid:id>/',views.update_products,name='update-product'),
    path('products/delete/<uuid:id>/',views.delete_products,name='delete-product'),
]