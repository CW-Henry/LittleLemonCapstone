from django.test import TestCase, Client

from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        MenuItem.objects.create(title="Dish1", price=15, inventory=500)
        MenuItem.objects.create(title="Dish2", price=25, inventory=50)
        MenuItem.objects.create(title="Dish3", price=150, inventory=5)

    def test_getall(self):
        response = self.client.get("/api/menu-items/")
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response, serializer.data)

    def test_getone(self):
        item = MenuItem.objects.create(title="DishA", price=50, inventory=25)
        response = self.client.get(f"/api/menu-items/{item.id}/")
        serializer = MenuItemSerializer(item, many=False)
        self.assertEqual(response.data, serializer.data)		