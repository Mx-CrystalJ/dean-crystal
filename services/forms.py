from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_id', 'service_id', 'order_description', 'word_count_range', 'total_price']

        widgets = {
            'user_id': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}), #RESEARCH MULTIPLE SERVICE SELECTION
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'word_count_range': forms.Select(attrs={'class': 'form-control'}),
            'total_price': forms.Select(attrs={'class': 'form-control'}), #RESEARCH SERVICE_ID PRICE SUM
        }