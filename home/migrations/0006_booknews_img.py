# Generated by Django 4.2.17 on 2025-01-02 09:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_authorswork_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booknews',
            name='img',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
