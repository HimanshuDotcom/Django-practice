from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "christmas/index.html",{
        "christmas": now.date == 25 and now.month == 12
    })