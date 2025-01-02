from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    #path('submit-testimonial/', views.submit_testimonial, name='submit_testimonial'),
]
