from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime

# Create your tests here.

class MenuTest(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(
            name="ice cream",
            price=15,
            menu_item_description="vanilla"
        )
        self.assertEqual(str(menu), "ice cream")
        self.assertEqual(menu.price, 15)
        self.assertEqual(menu.menu_item_description, "vanilla")

class BookingTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            first_name="Peter",
            reservation_date=datetime.now().date(),
            reservation_slot=12
        )
        self.assertEqual(str(booking), "Peter")
        self.assertEqual(booking.reservation_slot, 12)
