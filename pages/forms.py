from django import forms
from core.models import CustomUser

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email"]
