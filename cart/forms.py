from django import forms


class AddToCartForm(forms.Form):
    choices =[(i, str(i)) for i in range(1, 30)]
    quantity = forms.TypedChoiceField(choices=choices, coerce=int)
    
