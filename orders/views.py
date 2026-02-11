from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderProduct
from products.models import Product
from .forms import OrderProductForm
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_orders.html'
    context_object_name = 'order'
    
    def get_object(self, queryset=None):
        return Order.objects.filter(user=self.request.user, is_active=True).first()
    
class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/add_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('my_orders')
    
    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(user=self.request.user, is_active=True)
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
    
    
    def get_object(self, queryset=None):
        return Order.objects.filter(user=self.request.user, is_active=True).first()