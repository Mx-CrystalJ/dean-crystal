from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    """
    Model to store contact form submissions
    """
    STATUS_CHOICES = (
        ('unread', 'Unread'),
        ('read', 'Read'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )

    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='contact_submissions')  # Allow anonymous submissions
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, primary_key=True)
    enquiry_description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='unread')  # Add choices for status if needed

    def __str__(self):
        return f"{self.user_id.username if self.user_id else 'Anonymous'} - {self.subject}"