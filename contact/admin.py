from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('user_id', 'title', 'subject', 'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'title', 'subject',
                     'enquiry_description')
    actions = ['mark_as_read', 'mark_as_in_progress', 'mark_as_closed']

    def mark_as_read(self, request, queryset):
        """
        Action to mark selected contact submissions as "read"
        """
        queryset.update(status='read')

    mark_as_read.short_description = "Mark submissions as read"

    def mark_as_in_progress(self, request, queryset):
        """
        Mark "in_progress"
        """
        queryset.update(status='in_progress')

    mark_as_in_progress.short_description = "Mark submissions in progress"

    def mark_as_closed(self, request, queryset):
        """
        Mark "closed"
        """
        queryset.update(status='closed')

    mark_as_closed.short_description = "Mark submissions as closed"
