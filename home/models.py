from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsletterSubscriber(models.Model):
    """
    Model to store newsletter subscribers
    """
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, primary_key=True) 
    subscribed_date = models.DateTimeField(auto_now_add=True)
    terms_conditions = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class BookNews(models.Model):
    """
    Model to store book news items   
    """
    title = models.CharField(max_length=200)
    link = models.URLField() 
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """
    Model to store client testimonials
    """
    testimonial_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='testimonials')    
    content = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Testimonial from {self.user_id.username}"


    