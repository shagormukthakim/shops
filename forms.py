from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'buy_price', 'asking_price']

class SellProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['selling_price', 'sold_date']
