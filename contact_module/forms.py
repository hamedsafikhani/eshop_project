from django import forms

from .models import ContactUs


class ContactUsForm(forms.Form): # django forms fields
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=50,
        error_messages={
            'required' : 'لطفا نام را وارد کنید'
        },
        widget=forms.TextInput(attrs={
            'class' : 'form-control'
        })
    )
    email = forms.EmailField(label='ایمیل',widget=forms.EmailInput(attrs={
            'class' : 'form-control'
        }))
    title = forms.CharField(label='عنوان',widget=forms.TextInput(attrs={
            'class' : 'form-control'
        }))
    message = forms.CharField(label='متن پیام',widget=forms.Textarea(attrs={
            'class' : 'form-control',
            'id' : 'message'
        }))

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title','email','full_name','message']
        # fields = '__all__'
        # exclude = ['create_date','response','is_read_by_admin']
