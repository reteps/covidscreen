from django.shortcuts import render
from .models import (CovidScreen, CovidScreenInstance, Account, Event)
# Create your views here.

def index(request):
    ''' home page '''
    num_events = Event.objects.all().count()
    context = {
        "num_events": num_events
    }
    return render(request, "prescreen/index.html", context=context)