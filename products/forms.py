from django import forms
from .models import Products , Orders , Tag


class Form_Products(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'animal_type',
            'age_category',
            'tag',
            'name',
            'price',
            'description',
            'image',
       ]

        widgets = {
            'animal_type': forms.Select(attrs={'class': 'form-control'}),
            'age_category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', "rows":"3"}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class Form_Orders(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
            'name',
            'email',
            'phone',
            'address',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }