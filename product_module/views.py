from django.shortcuts import render,get_object_or_404
from .models import Product
# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request,'product_module/product_list.html',context={
        "products":products
    })


def product_detail(request,productId):
    product = get_object_or_404(Product,pk =productId)
    return render(request,'product_module/product_detail.html',context={
        'product' : product
    })