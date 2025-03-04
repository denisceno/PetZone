from django.contrib import admin
from .models import Products,AnimalType,AgeCategory,Orders,Tag

# Register your models here.
class AnimalTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('animal_type',)}

class AgeCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('age_category',)}

admin.site.register(Products)
admin.site.register(AnimalType,AnimalTypeAdmin)
admin.site.register(AgeCategory,AgeCategoryAdmin)
admin.site.register(Orders)
admin.site.register(Tag)