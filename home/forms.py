from django import forms
from .models import NewsletterSubscriber

class NewsletterForm(forms.ModelForm):
    """
    Form for users to subscribe to the newsletter
    """
    email = forms.EmailField(
        label='Email Address',
        required=True,  # Make the field required
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    terms_conditions = forms.BooleanField(
        label='I agree to the terms and conditions',
        required=True,  # Make the field required
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
    class Meta:
        model = NewsletterSubscriber
        fields = ['full_name', 'email', 'terms_conditions']  # Include the relevant fields

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
        }