from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """
    Form for users to submit contact requests
    """
    class Meta:
        model = Contact
        fields = ['title', 'subject', 'enquiry_description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'enquiry_description': forms.Textarea(attrs={'class': 'form-control'}),
        }
