from django.test import TestCase

from django.contrib.auth import get_user_model

from django.urls import reverse

from .models import Service, Customer

# Create your tests here.

class MoversTests(TestCase):
    """Test the models and the urls"""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            name = "A good name",
            email = "testname@email.com",
            phone_number = 712345678,
            bookin_id = 1,
            relocate_from = 'A good place',
            relocate_to = 'A good place',
            service = self.service,
    )

        self.service = Service.objects.create(
            name = "a good name",
            available_areas = "Good area locations"
    )

