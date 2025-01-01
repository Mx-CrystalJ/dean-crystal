from django.contrib import admin
from .models import Service, Order


# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_price', 'max_price', 'category', 'word_count_range', 'turnaround_time',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'service_id', 'order_description', 'word_count_range', 'order_date', 'total_price', 'status',)