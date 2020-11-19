from django.shortcuts import render
from .models import Flight, Airport
# Create your views here.
def index(request):
    return render(request, "flights/flights.html", {
        "flights": Flight.objects.all()
    })