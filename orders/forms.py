from django.forms import Textarea, ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address']
        widgets = {
            'address': Textarea(attrs={'cols': 30, 'rows': 5}),
        }