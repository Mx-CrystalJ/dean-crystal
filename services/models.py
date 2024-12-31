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
        ('author', 'Author Services'),
    )

    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    min_price = models.DecimalField(max_digits=8, decimal_places=2)
    max_price = models.DecimalField(max_digits=8, decimal_places=2, default=999.99)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    profile_image = CloudinaryField('image', default='placeholder')
    word_count_range = models.CharField(max_length=100, blank=True, null=True)
    turnaround_time = models.CharField(max_length=100, blank=True, null=True)
    formats_supported = models.CharField(max_length=200, blank=True, null=True)
    technologies_used = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Model to represent orders placed by users
    """
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    order_id = models.AutoField(primary_key=True)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='orders')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_description = models.TextField()
    word_count_range = models.CharField(max_length=100, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f"Order #{self.order_id} - {self.user_id.username} - {self.service_id.name}"