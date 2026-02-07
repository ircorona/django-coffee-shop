from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=255, label="Name")
    description = forms.CharField(max_length=300)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    available = forms.BooleanField(initial=True, label="Is Available",required=False)
    photo = forms.ImageField(required=False, label="Product Photo")
    
    def save(self):
        # Here you would typically save the form data to the database
        # For example, you could create a new Product instance and save it     
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo']
        )
        