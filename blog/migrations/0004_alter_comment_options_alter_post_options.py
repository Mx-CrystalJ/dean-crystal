# Generated by Django 4.2.17 on 2024-12-16 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_published']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated_on']},
        ),
    ]