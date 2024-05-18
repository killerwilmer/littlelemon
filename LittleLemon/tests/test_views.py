from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.contrib.auth.models import User

class TestMenuView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = APIClient()
    
        MenuItem.objects.create(title='Menu1', price=10.99, inventory=10)
        MenuItem.objects.create(title='Menu2', price=20.99, inventory=20)

    def test_getall(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('menu-items')
        response = self.client.get(url)
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)