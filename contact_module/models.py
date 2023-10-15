from django.db import models


# Create your models here.


class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام کامل')
    message = models.TextField(verbose_name='پیام')
    create_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='پاسخ ادمین', null=True, blank=True)
    is_read_by_admin = models.BooleanField(default=False,verbose_name='خوانده شده توسظ ادمین')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'




class UserProfile(models.Model):
    user_image = models.FileField(upload_to='images') # add to setting BASEDIR / images for media file