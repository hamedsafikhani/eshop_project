from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Product
from django.db.models import Avg
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'  # ba kilid product be template pass dadim age nazarim mishe object_list

    # ta inja kar mikone hame chi vali age bekhay filteri ijad koni bayad \/
    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data


class ProductListView1(TemplateView):
    template_name = 'product_module/product_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView1, self).get_context_data()
        context['products'] = Product.objects.all().order_by('-price')[:5]
        return context


# def product_list(request):
#     products = Product.objects.all().order_by('-price')[:5]
#     return render(request, 'product_module/product_list.html', context={
#         "products": products
#     })

# class ProductDetailView(TemplateView): ba estefade az TemplateView
#     template_name = 'product_module/product_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailView,self).get_context_data()
#         slug = kwargs['slug']
#         product = get_object_or_404(Product, slug=slug)
#         context['product'] = product
#         return context

class ProductDetailView(DetailView):  # ba estefade az Detail View
    # khodesh az url/slug ro barmidare va behtare ke az get_absolute_trl tooye model estefade she,ba pk <int:pk> ham mishe
    template_name = 'product_module/product_detail.html'
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object # dar list view ba in mitunim oon objecti ke khodesh entekhab karde ro vakeshi konim
        request = self.request # request ham darun khodesh dare
        product_id = request.session.get('favorite_product')
        context['is_favorite'] = product_id == str(loaded_product.id)
        return context


# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'product_module/product_detail.html', context={
#         'product': product
#     })

class AddFavoriteProduct(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session["favorite_product"] = product_id
        return redirect(product.get_absolute_url())
