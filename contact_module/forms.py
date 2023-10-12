from django import forms



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
    subject = forms.CharField(label='عنوان',widget=forms.TextInput(attrs={
            'class' : 'form-control'
        }))
    text = forms.CharField(label='متن پیام',widget=forms.Textarea(attrs={
            'class' : 'form-control',
            'id' : 'message'
        }))