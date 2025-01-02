from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post  # Blog posts are in the 'blog' app
from .models import NewsletterSubscriber, BookNews, Testimonial, AuthorsWork #Custom Models
from .forms import NewsletterForm, TestimonialForm
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
            messages.success(request, 'Thank you! You are subscribed to the Dean Crystal publishing and technology newsletter!')
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

def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user_id = request.user
            testimonial.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you, your testimonial has been submitted and is awaiting approval!')
        return redirect('home')
    else:
        form = TestimonialForm()
    return render(request, 'home/home.html', {'form': form})