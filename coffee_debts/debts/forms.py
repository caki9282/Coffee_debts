from django import forms
from django.forms import ModelForm
from .models import CoffeePurchase
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from .models import CoffeePurchase
from decimal import Decimal
from django.contrib.auth import get_user_model

class CoffeePurchaseForm(forms.ModelForm):
    class Meta:
        model = CoffeePurchase
        fields = ['cost']
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class BatchCoffeePurchaseForm(forms.Form):
    entries = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Username:Cost (one per line)'}), help_text="Enter each purchase as 'Username:Cost' on a new line.")

class CoffeeCostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CoffeeCostForm, self).__init__(*args, **kwargs)
        users = get_user_model().objects.all()
        for user in users:
            self.fields[f'{user.username}_cost'] = forms.DecimalField(
                label=f"{user.username}'s coffee cost", 
                min_value=0.01, 
                max_digits=6, 
                decimal_places=2, 
                required=False,
                widget=forms.NumberInput(attrs={'class': 'custom-input', 'placeholder': f'{user.username}\'s Cost'}))