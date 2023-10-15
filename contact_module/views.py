from django.views.generic import FormView, CreateView, ListView
from .forms import  ContactUsModelForm
from .models import UserProfile


# Create your views here.

class ContactUsView(CreateView):  # niaz be zakhire o form valid ina nadare chon create hast khodesh save mikone.
    template_name = 'contact_module/contact_us_page.html'
    # model = ContactUs #mitune comment bashe ya nabashe chon form ma az noe modelform hast
    form_class = ContactUsModelForm
    success_url = '/contact-us/'



###########################temp
# def store_file(file): # handle file by python
#     with open('temp/image.jpg','wb+') as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
class ProfileImage(CreateView): # by CreateView
    template_name = 'contact_module/profile-image.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/profile-image'


class ProfilesView(ListView):
    template_name = 'contact_module/profiles_page.html'
    model = UserProfile
    context_object_name = 'products'
###########################temp
