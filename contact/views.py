from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact_me(request):
    return HttpResponse('Hello, Contact!')