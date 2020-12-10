from django.shortcuts import render
from .models import Event, Account, CustomQuestionResponse, Response, CustomQuestion
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    ''' home page '''
    context = {
        "events": Event.objects.all()
    }
    # TODO Pagination
    
    return render(request, "prescreen/home.html", context=context)

class EventDetail(LoginRequiredMixin, generic.DetailView):
    model = Event
    template_name = "prescreen/event_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_creator'] = self.request.user.id == self.object.creator.id
        return context

class EventUpdate(generic.UpdateView):
    model = Event
    fields = '__all__'

class EventCreate(generic.CreateView):
    # uses modelname_form.html
    model = Event
    fields = ['title', 'start_time']