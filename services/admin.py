from django.contrib import admin
from .models import Service, Order
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('name', 'min_price', 'max_price', 'category', 'word_count_range', 'turnaround_time',)
    search_fields = ['name', 'category']
    list_filter = ('category', 'turnaround_time',)

@admin.register(Order)
class OrderAdmin(SummernoteModelAdmin):
    list_display = ('user_id', 'service_id', 'order_description', 'word_count_range', 'order_date', 'total_price', 'status',)
    search_fields = ['user_id', 'order_date']
    list_filter = ('status', 'order_date',)