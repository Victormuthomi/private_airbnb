from django.contrib import admin

from .models import Service, Customer, OtherServices

# Register your models here.

admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(OtherServices)
