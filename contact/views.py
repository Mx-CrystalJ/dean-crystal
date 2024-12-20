from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact_me(request):
    """
    A view to return the contact page
    """
    return render(request, 'contact/contact.html')