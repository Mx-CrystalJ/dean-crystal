from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Service, Order
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Service, Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



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
            # Calculate estimated total_price based on service's min and max prices
        
            service = order.service_id
            min_price = service.min_price
            max_price = service.max_price

            # Example calculation (replace with your actual logic)
            order.total_price = (min_price + max_price) / 2  # Average of min and max
            order.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Order submitted and awaiting approval! You will be contacted within 48hrs!')
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
            messages.add_message(
            request, messages.SUCCESS,
            'Order edit submitted and awaiting approval! You will be contacted within 24hrs!')
            return redirect('services')
    else:
        form = OrderForm(instance=order)
    return render(request, 'services/edit_order.html', {'form': form, 'order': order})


def delete_order(request, order_id):
    """
    View to delete an order
    """
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    messages.add_message(
            request, messages.SUCCESS,
            'Your order was successfully deleted!')
    return redirect('services')

@login_required 
def orders(request):
    """
    A view to display the logged in user's orders
    """
    orders = Order.objects.filter(user_id=request.user)  # Get logged-in user's orders
    return render(request, 'services/orders.html', {'orders': orders})