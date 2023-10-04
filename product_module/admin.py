#user admin pass admin123
from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ['title']
    }

admin.site.register(models.Product,ProductAdmin)