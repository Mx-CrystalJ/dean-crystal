# Generated by Django 4.2.17 on 2024-12-30 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='word_count_range',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
