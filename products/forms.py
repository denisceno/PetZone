from django import forms
from .models import Products


class Form_Products(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'animal_type',
            'age_category',
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
