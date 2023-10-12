from django import forms



class ContactUsForm(forms.Form): # django forms fields
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=50,
        error_messages={
            "required" : 'لطفا نام را وارد کنید'
        }
    )
    email = forms.EmailField(label='ایمیل',widget=forms.EmailInput)
    subject = forms.CharField(label='عنوان')
    text = forms.CharField(label='متن پیام',widget=forms.Textarea)