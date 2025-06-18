from django.db import models
import uuid


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

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    
class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal_type = models.ForeignKey(AnimalType,on_delete=models.CASCADE)
    age_category = models.ForeignKey(AgeCategory,on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(Tag, null=True ,blank=True,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)


    def __str__(self):
        return f'{self.name}  {self.price}'
    

class Orders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()


    def __str__(self):
        return f'{self.product}  {self.order_date}'