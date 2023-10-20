# Generated by Django 4.2.5 on 2023-10-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0002_alter_contactus_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.FileField(upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='contactus',
            name='is_read_by_admin',
            field=models.BooleanField(default=False, verbose_name='خوانده شده توسظ ادمین'),
        ),
    ]
