from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Avg


# Create your views here.


def product_list(request):
    products = Product.objects.all().order_by('-price')
    number_of_products = products.count()
    # avg_of_rating = products.aggregate(Avg('rating')) # aggregate( avg , min , max and ... )

    return render(request, 'product_module/product_list.html', context={
        "products": products,
        "number_of_products": number_of_products
        # "avg_of_rating" : avg_of_rating
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_module/product_detail.html', context={
        'product': product
    })
