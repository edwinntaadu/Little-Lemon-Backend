from django.test import TestCase
from .models import Menu
from .serializers import MenuSerializer

class MenuItemViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=10, inventory=20)
        Menu.objects.create(title="Burger", price=8, inventory=15)
    
    def test_getall(self):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)