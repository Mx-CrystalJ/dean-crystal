from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.
def contact_me(request):
    """
    A view to display the contact page and handle form submission
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_submission = form.save(commit=False)
            if request.user.is_authenticated:
                contact_submission.user = request.user
            contact_submission.save()
            return redirect('contact_success')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)