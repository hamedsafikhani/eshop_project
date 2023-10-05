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

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural =  'دسته بندی ها'

class ProductInformation(models.Model):
    color = models.CharField(max_length=10,verbose_name='رنگ')
    size = models.CharField(max_length=10,verbose_name='سایز')

    def __str__(self):
        return f'{self.color}-{self.size}'
    class Meta:
        verbose_name = 'اطلاعات محصول'
        verbose_name_plural = 'تمامی اطلاعات محصول'
class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        null=True,
        related_name='products'
    )
    product_information = models.OneToOneField(
        ProductInformation,
        on_delete=models.CASCADE,
        related_name='product_information',
        verbose_name='اطلاعات تکمیلی',
        null=True,blank=True)
    price = models.IntegerField()
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    short_description = models.CharField(
        max_length=360,
        null=True
    )
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(
        default='',
        null=False,
        db_index=True
    ) # db_index = True : busy field for speed queries to DB

    def get_absolute_url(self):
        return reverse('product_detail',args=[self.slug])

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

