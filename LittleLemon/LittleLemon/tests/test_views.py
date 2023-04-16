from django.test import TestCase, Client
from rest_framework.test import APIClient

# from LittleLemonAPI.models import MenuItem
# from LittleLemonAPI.serializers import MenuItemSerializer
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        Menu.objects.create(title="Dish1", price=15, inventory=500)
        Menu.objects.create(title="Dish2", price=25, inventory=50)
        Menu.objects.create(title="Dish3", price=150, inventory=5)
        self.user = User.objects.create(
            username="tempadmin",
            password="pass",
        )
        self.client.force_authenticate(self.user)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_getone(self):
        item = Menu.objects.create(title="DishA", price=50, inventory=25)
        response = self.client.get(f"/restaurant/menu/{item.id}")
        serializer = MenuSerializer(item, many=False)
        self.assertEqual(response.data, serializer.data)
