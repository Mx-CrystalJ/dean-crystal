from django.shortcuts import render
from blog.models import Post  # Blog posts are in the 'blog' app
from .models import NewsletterSubscriber, BookNews
from .forms import NewsletterForm

def index(request):
    """
    A view to return the home page and the blog post list
    """
    posts = Post.objects.all()  # Retrieve all blog posts
    newsletter_form = NewsletterForm()  # Create an instance of your newsletter form
    book_news = BookNews.objects.all()  # Retrieve all book news items

    if request.method == 'POST':  # Handle newsletter form submission
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            # Add this line to clear the form after successful submission:
            newsletter_form = NewsletterForm()  

    context = {
        'posts': posts,
        'newsletter_form': newsletter_form,  # Pass the form to the template
        'book_news': book_news,  # Pass the book news items to the template
    }
    return render(request, 'home/home.html', context)