from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان')
    url_title = models.CharField(max_length=300,verbose_name='عنوان url')

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    short_description = models.CharField(max_length=360,null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default='',null=False,db_index=True) # db_index = True : busy field for speed queries to DB
    color = models.CharField(default='white',null=True,max_length=10)
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.slug])

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title}"

