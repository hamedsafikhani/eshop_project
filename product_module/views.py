from django.shortcuts import render,get_object_or_404
from .models import Product
# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request,'product_module/product_list.html',context={
        "products":products
    })


def product_detail(request,slug):
    product = get_object_or_404(Product,slug =slug)
    return render(request,'product_module/product_detail.html',context={
        'product' : product
    })