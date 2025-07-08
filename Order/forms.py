from django import forms
from .models import Product

class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1, initial=1)

class FinalizeOrderForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea, required=True)
