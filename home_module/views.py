from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.

#
# def index(request):
#     return render(request,'home_module/index_page.html')

# class HomeView(View): # use View
#     def get(self,request):
#         return render(request,'home_module/index_page.html')
class HomeView(TemplateView):
    template_name = 'home_module/index_page.html' #BARAYE load shodan template ta haminja kafie
    #age bekhaym data be template pass bedim
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['data'] = 'this is home page data'
        return context




def site_header_component(request): #pip3 install django-render-partial
    return render(request,'shared/site_header_component.html')

def site_footer_component(request):
    return render(request,'shared/site_footer_component.html')