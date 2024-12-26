from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Service(models.Model):
    """
    Model to represent the services offered
    """
    CATEGORY_CHOICES = (
        ('editing', 'Editing and Proofreading'),
        ('formatting', 'Book Formatting'),
        ('webdev', 'Web Development'),
    )

    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    profile_image = CloudinaryField('image', default='placeholder')
    word_count_range = models.CharField(max_length=100, blank=True, null=True)
    turnaround_time = models.CharField(max_length=100, blank=True, null=True)
    formats_supported = models.CharField(max_length=200, blank=True, null=True)
    technologies_used = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name