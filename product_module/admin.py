#user admin pass admin123
from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Product)