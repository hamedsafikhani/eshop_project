from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# baraye migrate bayad aval hame app ha disable beshan tu setting va usrls asli proje bad amaliate migrate va DB pak she (aval kar bayad inkaro kard
class User(AbstractUser): # ezafe field be model user khode django
    mobile = models.CharField(max_length=20,verbose_name='تلفن همراه')
    email_active_code = models.CharField(max_length=200,verbose_name='کد فعال سازی')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()