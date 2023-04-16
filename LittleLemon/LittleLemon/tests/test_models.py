from django.test import TestCase
# from LittleLemonAPI.models import MenuItem
from restaurant.models import Menu


# class MenuItemTest(TestCase):
#     def test_get_item(self):
#         item = MenuItem.objects.create(
#             title="IceCream", price=80, inventory=100)
#         itemstr = item.get_item()

#         self.assertEqual(itemstr, "IceCream : 80")

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="IceCream", price=80, inventory=100)

        self.assertEqual(str(item), "IceCream : 80")
