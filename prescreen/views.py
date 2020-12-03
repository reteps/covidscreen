from django.shortcuts import render
from .models import Event, Account, CustomQuestionResponse, Response, CustomQuestion

def index(request):
    ''' home page '''
    context = {
        "events": Event.objects.all()
    }
    # TODO Pagination
    
    return render(request, "prescreen/index.html", context=context)