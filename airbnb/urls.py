from django.urls import path 

from .views import AirbnbListView, HomeListView, CustomerListView,BookedListView,AirbnbDetailView, customer_create_view

urlpatterns =[
    path('', HomeListView.as_view(), name ='home'),
    path('airbnb/', AirbnbListView.as_view(), name= 'airbnb'),
    path('airbnb_customer/', CustomerListView.as_view(), name = 'airbnb_customer'),
    path('airbnb_customer_form/', customer_create_view, name = 'airbnb_customer_form'),
    path('booked/', BookedListView.as_view(), name='booked'),
    path('airbnb/<int:pk>/', AirbnbDetailView.as_view(), name='airbnb_detail'),


]

