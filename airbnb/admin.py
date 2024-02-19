from django.contrib import admin

from .models import Airbnb, Customer,  Airbnbimage, OtherServicesBooking, OtherService, HomepageImages

# Register your models here.

admin.site.register(Airbnb)
admin.site.register(Customer)
admin.site.register(Airbnbimage)
admin.site.register(OtherServicesBooking)
admin.site.register(OtherService)
admin.site.register(HomepageImages)

