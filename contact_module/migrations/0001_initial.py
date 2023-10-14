# Generated by Django 4.2.5 on 2023-10-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('email', models.EmailField(max_length=300, verbose_name='ایمبل')),
                ('full_name', models.CharField(max_length=300, verbose_name='نام کامل')),
                ('message', models.TextField(verbose_name='پیام')),
                ('is_read_by_admin', models.BooleanField(verbose_name='خوانده شده توسظ ادمین')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('response', models.TextField(blank=True, null=True, verbose_name='پاسخ ادمین')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
    ]
