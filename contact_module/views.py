from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, CreateView

from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs


# Create your views here.

class ContactUsView(CreateView):  # niaz be zakhire o form valid ina nadare chon create hast khodesh save mikone.
    template_name = 'contact_module/contact_us_page.html'
    # model = ContactUs #mitune comment bashe ya nabashe chon form ma az noe modelform hast
    form_class = ContactUsModelForm
    success_url = '/contact-us/'


# class ContactUsView(FormView):
#     template_name = 'contact_module/contact_us_page.html'
#     form_class = ContactUsModelForm
#     success_url = '/contact-us/'  # bade submit koja bere
#
#     def form_valid(self, form):  # age valid bud chi kone (validation ro khodesh anjam mide)
#         form.save()  # zakhire to DB
#         return super().form_valid(form)  # hatman bayad bezari
#
#     def form_invalid(self, form):
#         pass

# class ContactUsView(View):
#     def get(self, request):
#         contact_form = ContactUsModelForm()
#         return render(request, 'contact_module/contact_us_page.html', {
#             'contact_form': contact_form
#         })
#
#     def post(self, request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('home_page')
#
#         return render(request, 'contact_module/contact_us_page.html', {
#             'contact_form': contact_form
#         })

# def contact_page(request):
#     if request.method == 'POST':
#         # contact_form = ContactUsForm(request.POST)
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             print(contact_form.cleaned_data)
#             # contact = ContactUs(
#             #     title = contact_form.cleaned_data.get('title'),
#             #     email = contact_form.cleaned_data.get('email'),
#             #     full_name = contact_form.cleaned_data.get('full_name'),
#             #     message = contact_form.cleaned_data.get('message')
#             # )
#             # contact.save()
#             contact_form.save()
#             return redirect('home_page')
#
#     else:
#         # contact_form = ContactUsForm()
#         contact_form = ContactUsModelForm()
#     return render(request,'contact_module/contact_us_page.html',{
#         'contact_form' : contact_form
#     })


###########################temp
class ProfileImage(View):
    def get(self, request):
        return render(request, 'contact_module/profile-image.html')

    def post(self, request):
        print(request.FILES)
        return redirect('/contact-us/profile-image')

###########################temp
