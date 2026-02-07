from django.urls import path
from .views import ProductFormView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_form'),
    path('add/', ProductFormView.as_view(), name='add_product'),
]
