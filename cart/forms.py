from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 1:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity
    
