from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404

from django.views.generic import ListView, TemplateView, DetailView

from .models import Airbnb,Customer, HomepageImages

from .forms import CustomerForm

# Create your views here.

class HomeListView(TemplateView):
    """Define the template to use for the homepage"""
    template_name = 'home.html'

class BookedListView(TemplateView):
    """Define the template to be returned after a user books an airbnb."""
    template_name = 'booked.html'


class AirbnbListView(ListView):
    """Define the model and the template to use for the airbnbs"""
    model = Airbnb
    template_name = 'airbnb.html'
    context_object_name = 'all_airbnbs_list'



class CustomerListView(ListView):
    """Define the model and temlate to use for the customers"""
    model = Customer 
    template_name = 'airbnb_customer.html'


def customer_create_view(request, airbnb_id=None):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booked')
    else:
        airbnb = get_object_or_404(Airbnb, id=airbnb_id) if airbnb_id else None
        form = CustomerForm(initial={'airbnb': airbnb})

    return render(request, 'airbnb_customer_form.html', {'form': form, 'airbnb': airbnb})


def home(request):
    images = HomepageImages.objects.all()
    return render(request, 'home.html', {'images': images})

class AirbnbDetailView(DetailView):
    model = Airbnb
    template_name = 'airbnb_detail.html'