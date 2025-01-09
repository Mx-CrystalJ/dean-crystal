from django.contrib import admin
from .models import NewsletterSubscriber, BookNews, Testimonial, AuthorsWork
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(SummernoteModelAdmin):
    list_display = (
        'full_name', 'email', 'subscribed_date', 'terms_conditions')
    search_fields = ('full_name', 'email')
    list_filter = ('subscribed_date', 'terms_conditions')


@admin.register(BookNews)
class BookNewsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'link', 'publication_date')
    search_fields = ('title', 'link')
    list_filter = ('publication_date',)


@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):
    list_display = ('user_id', 'content', 'approved')
    search_fields = ('user__username', 'content')
    actions = ['approve_testimonials']
    summernote_fields = ('content',)

    def approve_testimonials(self, request, queryset):
        """
        Action to approve selected testimonials
        """
        queryset.update(approved=True)

    approve_testimonials.short_description = "Approve selected testimonial"


@admin.register(AuthorsWork)
class AuthorsWorkAdmin(SummernoteModelAdmin):
    list_display = ('author_name', 'title', 'work_location', 'work_url', 'img')
    search_fields = ('author_name', 'title', 'work_description')
    list_filter = ('author_name', 'work_location',)
    fields = ('author_name', 'title', 'img', 'work_description', 'work_url',
              'work_location')
    summernote_fields = ('work_description',)
