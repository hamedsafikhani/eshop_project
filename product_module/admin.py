# user admin pass admin123
from django.contrib import admin
from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }

    list_display = ['title','price','rating','is_active','category']
    list_filter = ['rating','is_active']
    list_editable = ['price','rating','is_active','category']



admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductInformation)
