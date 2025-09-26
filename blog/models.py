from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, default='images/no_image_available.png') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
