from django.shortcuts import render, redirect
from . models import Menu, Reservation
from django.http import HttpResponseRedirect
from .forms import ReservationForm
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, 'hotel/index.html', {})

def menu_view(request):
    items = Menu.objects.all()
    return render(request, 'restaurant/menu.html', {'items': items})





def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Create and save a Reservation object
            reservation = Reservation(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                date=data['date'],
                time=data['time'],
                number_of_people=data['number_of_people'],
                message=data.get('message', '')  # Handle optional message field
            )
            reservation.save()
            return redirect('thank_you')  # Redirect to a thank-you page
    else:
        form = ReservationForm()
    
    return render(request, 'hotel/reservation.html', {'form': form})

