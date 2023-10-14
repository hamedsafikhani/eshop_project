
from django.urls import path
from . import views

urlpatterns = [
    path('',views.ContactUsView.as_view(),name='contact_us_page'),
    path('profile-image',views.ProfileImage.as_view(),name='profile_image')
]