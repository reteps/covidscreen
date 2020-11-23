from django.shortcuts import render
from .models import Event, Account, QuestionSet, CovidScreenData, Response

def index(request):
    ''' home page '''
    num_events = Event.objects.all().count()
    context = {
        "num_events": num_events
    }
    return render(request, "prescreen/index.html", context=context)