# Generated by Django 4.2.17 on 2024-12-27 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_authorswork'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorswork',
            name='author_name',
            field=models.CharField(default='Dean Crystal', max_length=100),
        ),
    ]
