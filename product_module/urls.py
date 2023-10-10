from django.urls import path
from . import views


urlpatterns = [
    path('',views.product_list,name=''),
    path('<slug:slug>',views.product_detail,name="product_detail"),
]