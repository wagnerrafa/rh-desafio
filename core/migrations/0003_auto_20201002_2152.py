# Generated by Django 3.1.1 on 2020-10-02 21:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201002_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Foto de logo'),
        ),
    ]
