from django import forms
from .models import Customer, OtherServicesBooking


class CustomerForm(forms.ModelForm):
     """Initialize the fields for the customer template"""
     class Meta:
          model = Customer
          fields = ['name', 'email', 'phone_number', 'airbnb']

class OtherServicesForm(forms.ModelForm):
     """Initialize the fields for otherservices """
     class Meta:
          model = OtherServicesBooking
          fields = ['name', 'email', 'phone_number','service_name']



     