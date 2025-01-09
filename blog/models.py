from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author_id}"


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_published"]

    def __str__(self):
        return f"Comment {self.body} by {self.author_id}"
