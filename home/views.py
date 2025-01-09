from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from .models import NewsletterSubscriber, BookNews, Testimonial, AuthorsWork
from .forms import NewsletterForm
from django.contrib import messages


def index(request):
    """
    A view to return the home page, blog posts,
    newsletter form, book news items, testimonials, and author's works.
    """
    posts = Post.objects.all()
    newsletter_form = NewsletterForm()
    book_news = BookNews.objects.all()
    testimonials = Testimonial.objects.all()
    authors_works = AuthorsWork.objects.all()

    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(
                request, 'You are subscribed to the Dean Crystal newsletter!')
            newsletter_form = NewsletterForm()

    context = {
        'posts': posts,
        'newsletter_form': newsletter_form,
        'book_news': book_news,
        'testimonials': testimonials,
        'authors_works': authors_works,
    }
    return render(request, 'home/home.html', context)


def terms_conditions(request):
    """
    A view to return the terms and conditions page
    """
    return render(request, 'home/terms_conditions.html')
