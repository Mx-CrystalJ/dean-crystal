from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def service(request):
    """
    A view to return the contact page
    """
    return render(request, 'services/services.html')