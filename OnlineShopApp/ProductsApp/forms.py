from django import forms

from ProductsApp.models import Product


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'