from django.shortcuts import render
from blog.models import Post  # Assuming your blog posts are in the 'blog' app

def index(request):
    """
    A view to return the home page and the blog post list
    """
    posts = Post.objects.all()  # Retrieve all blog posts

    context = {
        'posts': posts,
    }
    return render(request, 'home/home.html', context)