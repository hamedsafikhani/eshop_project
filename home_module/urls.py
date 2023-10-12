from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home_page'),
    path('contact-us',views.contact_page)
    # path('site-header-component',views.site_header_component) # yeki az rah ha baraye render partial
]