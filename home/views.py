from django.shortcuts import render, redirect
from blog.models import Post  # Blog posts are in the 'blog' app
from .models import NewsletterSubscriber, BookNews, Testimonial, AuthorsWork
from .forms import NewsletterForm, TestimonialForm

def index(request):
    """
    A view to return the home page and the blog post list
    """
    posts = Post.objects.all()  # Retrieve all blog posts
    newsletter_form = NewsletterForm()  # Create an instance of your newsletter form
    book_news = BookNews.objects.all()  # Retrieve all book news items
    testimonials = Testimonial.objects.all()  # Retrieve all testimonials
    authors_works = AuthorsWork.objects.all() # Retrieve all author's works

    if request.method == 'POST':  # Handle newsletter form submission
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            newsletter_form = NewsletterForm()  

    context = {
        'posts': posts,
        'newsletter_form': newsletter_form,  # Pass the form to the template
        'book_news': book_news,  # Pass the book news items to the template
        'testimonials': testimonials,  # Add testimonials to the context
        'authors_works': authors_works,  # Add authors_works to the context
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
            testimonial.user_id = request.user  # Set the logged-in user
            testimonial.save()
            return redirect('testimonials')  # Redirect to the testimonials page
    else:
        form = TestimonialForm()
    return render(request, 'home/submit_testimonial.html', {'form': form})