from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post  # Blog posts are in the 'blog' app
from .models import NewsletterSubscriber, BookNews, Testimonial, AuthorsWork #Custom Models
from .forms import NewsletterForm, TestimonialForm

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
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            newsletter_form = NewsletterForm()  

    context = {
        'posts': posts,
        'newsletter_form': newsletter_form,  # Pass the form to the template by adding to the context.
        'book_news': book_news,
        'testimonials': testimonials,
        'authors_works': authors_works,
    }
    return render(request, 'home/home.html', context)


def terms_conditions(request):
    """
    A view to return the terms and conditions page
    """
    return render(request, 'home/terms&conditions.html')

def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user_id = request.user
            testimonial.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'home/submit_testimonial.html', {'form': form})