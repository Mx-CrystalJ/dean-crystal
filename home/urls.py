from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog-urls'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    path('submit-testimonial/', views.submit_testimonial, name='submit_testimonial'),
]
