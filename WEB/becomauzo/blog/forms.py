from django import forms
from blog.models import *


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            "category",
            "name",
            "price",
            "discount_price",
            "product_available_count",
            "description",
            "available",
            
            "image"
            ]