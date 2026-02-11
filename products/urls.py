from django.urls import path
from .views import ProductFormView, ProductListView, ProductListAPI

urlpatterns = [
    path('', ProductListView.as_view(), name='product_form'),
    path('api/', ProductListAPI.as_view(), name='product_list_api'),
    path('add/', ProductFormView.as_view(), name='add_product'),
]
