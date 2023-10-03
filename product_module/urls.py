from django.urls import path
from . import views


urlpatterns = [
    path('',views.product_list),
    path('<int:productId>',views.product_detail,name="product_detail"),
]