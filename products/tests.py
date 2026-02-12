from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductListViewTests(TestCase):
    def test_should_return_200(self):
        url = reverse("product_form")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"].count(), 0)

    def test_should_return_200_with_products(self):
        url = reverse("product_form")
        Product.objects.create(
            name="Espresso",
            description="Strong and bold coffee",
            price=2.5,
            available=True,
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"].count(), 1)
