from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Avg
from django.views.generic import TemplateView,ListView


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products' # ba kilid product be template pass dadim age nazarim mishe object_list

    #ta inja kar mikone hame chi vali age bekhay filteri ijad koni bayad \/
    def get_queryset(self):
        base_query = super(ProductListView,self).get_queryset()
        data = base_query.filter(is_active=True)
        return data



class ProductListView1(TemplateView):
    template_name = 'product_module/product_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView1,self).get_context_data()
        context['products'] = Product.objects.all().order_by('-price')[:5]
        return context

# def product_list(request):
#     products = Product.objects.all().order_by('-price')[:5]
#     return render(request, 'product_module/product_list.html', context={
#         "products": products
#     })

class ProductDetailView(TemplateView):
    template_name = 'product_module/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView,self).get_context_data()
        slug = kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        context['product'] = product
        return context
# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'product_module/product_detail.html', context={
#         'product': product
#     })
