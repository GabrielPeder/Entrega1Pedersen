from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    model = forms.IntegerField()
    price = forms.IntegerField()
    stock = forms.BooleanField(required=False)