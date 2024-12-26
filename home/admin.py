from django.contrib import admin
from .models import NewsletterSubscriber, BookNews


# Register your models here.
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subscribed_date', 'terms_conditions')
    search_fields = ('full_name', 'email')
    list_filter = ('subscribed_date', 'terms_conditions')


@admin.register(BookNews)
class BookNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'publication_date')
    search_fields = ('title', 'link')
    list_filter = ('publication_date',)