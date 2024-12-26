from django.shortcuts import render
from django.http import HttpResponse
from .models import Service


# Create your views here.
def service(request):
    """
    A view to return the contact page
    """
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'services/services.html', context)