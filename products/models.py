from django.db import models
import uuid

# Create your models here.

class AnimalType(models.Model):
    animal_type = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.animal_type
    
class AgeCategory(models.Model):
    age_category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.age_category


    
class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal_type = models.ForeignKey(AnimalType,on_delete=models.CASCADE)
    age_category = models.ForeignKey(AgeCategory,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)



