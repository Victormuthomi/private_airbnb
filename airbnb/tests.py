from django.contrib.auth import get_user_model

from django.test import TestCase

from django.urls import reverse

from .models import Airbnb, Customer, Airbnbimage
# Create your tests here.

class AirbnbTests(TestCase):
    """Tests for the models and urls"""
    def setUp(self):
        self.airbnb = Airbnb.objects.create(
            name = "A good name",
            location = "a good location name",
            rooms = 5,
            price = 100.00,
            avalability = True,
            services = 'A good service',
        )

        self.user = get_user_model().objects.create_user(
            name = "A good name",
            email = "testname@email.com",
            phone_number = 712345678,
            bookin_id = 1,
            airbnb = self.airbnb,
        )


