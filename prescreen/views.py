from django.shortcuts import render
from .models import Event, Account, CustomQuestionResponse, Response, CustomQuestion
from django.views import generic

def home(request):
    ''' home page '''
    context = {
        "events": Event.objects.all()
    }
    # TODO Pagination
    
    return render(request, "prescreen/home.html", context=context)

class EventDetailView(generic.DetailView):
    model = Event
