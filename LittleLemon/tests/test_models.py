from django.test import TestCase
from restaurant.models import MenuItem


class TestMenuItem(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Test Item", price=5.99, inventory=10)
        self.assertEqual(item.get_item(), "Test Item : 5.99")