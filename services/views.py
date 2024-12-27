from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Service, Order
from .forms import OrderForm


# Create your views here.
def service(request):
    """
    A view to return the services page and handle order creation
    """
    services = Service.objects.all()
    order_form = OrderForm()

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user_id = request.user_id  # Set the logged-in user
            # ... (Calculate total_price based on the selected service, etc.) ...
            order.save()
            return redirect('services')

    context = {
        'services': services,
        'order_form': order_form,
    }
    return render(request, 'services/services.html', context)