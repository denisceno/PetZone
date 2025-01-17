from django import forms
from .models import BlogPost

class StoryForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']
