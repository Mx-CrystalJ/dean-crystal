from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Order
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
            order.user_id = request.user
            # ... (Calculate total_price based on the selected service, etc.) ...
            order.save()
            return redirect('services')

    context = {
        'services': services,
        'order_form': order_form,
    }
    return render(request, 'services/services.html', context)


def edit_order(request, order_id):
    """
    View to edit an order
    """
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'services/edit_order.html', {'form': form, 'order': order})


def delete_order(request, order_id):
    """
    View to delete an order
    """
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect('orders')
