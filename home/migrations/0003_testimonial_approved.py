# Generated by Django 4.2.17 on 2024-12-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]