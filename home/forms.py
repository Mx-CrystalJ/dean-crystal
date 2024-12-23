from django import forms
from .models import NewsletterSubscriber

class NewsletterForm(forms.ModelForm):
    """
    Form for users to subscribe to the newsletter
    """
    class Meta:
        model = NewsletterSubscriber
        fields = ['full_name', 'email', 'terms_conditions']  # Include the relevant fields

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'terms_conditions': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'terms_conditions': 'I agree to the terms and conditions', 
        }