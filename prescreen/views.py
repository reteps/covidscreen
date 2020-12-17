from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from .models import Event, Account, CustomQuestionResponse, Response, CustomQuestion
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from prescreen.forms import ResponseForm, EventCreateForm, EventJoinForm
import datetime
class AllEventList(generic.ListView):
    model = Event
    template = "prescreen/event_list.html"
    context_object_name = 'events'
class UserEventList(LoginRequiredMixin, generic.ListView):
    model = Event
    template = "prescreen/home.html"
    context_object_name = 'events'
    def get_queryset(self):
        return self.request.user.account.events.all()
class EventDetail(LoginRequiredMixin, generic.DetailView):
    model = Event
    template_name = "prescreen/event_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_creator'] = self.request.user.id == self.object.creator.id
        my_response = Response.objects.filter(event=self.kwargs['pk'], account=self.request.user.account)[0]
        print(my_response.get_absolute_url())
        context['my_response'] = my_response
        return context

class ResponseDetail(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Response
    def test_func(self):
        response = self.get_object()
        if self.request.user.account == response.account or self.request.user.account == response.event.creator:
            return True
        return False
class ResponseUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Response
    fields = ['temperature', 'contact_with_covid']
    def test_func(self):
        response = self.get_object()
        if self.request.user.account == response.account:
            return True
        return False
class EventResponseList(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Response
    # template = "prescreen/response_list.html"
    def test_func(self):
        event = Event.objects.get(uuid=self.kwargs.get('event'))
        if self.request.user.account == event.creator:
            return True
        return False
    def get_queryset(self):
        return Response.objects.filter(event__uuid=self.kwargs.get('event'))
    # Note that get_queryset could also be overriden
class EventUpdate(generic.UpdateView):
    model = Event
    fields = ['title', 'start_time']

@login_required
def join_event(request):
    if request.method == 'POST':
        form = EventJoinForm(request.POST)
        if form.is_valid():
            event_uuid = form.cleaned_data['code']
            event = Event.objects.get(uuid=event_uuid)
            print('Join Event', event)
            request.user.account.events.add(event)
            request.user.account.save()
            return redirect('home')
    else:
        form = EventJoinForm()
    return render(request, 'prescreen/event_join.html', {'form': form})

class EventCreate(LoginRequiredMixin, generic.CreateView):
    # uses modelname_form.html
    model = Event
    form_class = EventCreateForm

    def form_valid(self, form):
        form.instance.creator = self.request.user.account
        print('Create event:',form.instance)
        self.request.user.account.events.add(form.instance)
        self.request.user.account.save()
        return super().form_valid(form)
'''
@login_required
def create_response(request, event):
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.event = event
            response.account = request.user.account
            response.save()
            messages.success(request, 'Your response has been recorded')
            # return HttpResponseRedirect(reverse('home'))
            return redirect('home')
    else:
        form = ResponseForm()
    return render(request, 'prescreen/response_form.html', {'form': form})

'''
class ResponseCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Response
    form_class = ResponseForm
    template_name = 'prescreen/response_form.html'
    # fields = ['temperature', 'contact_with_covid']
    # Only allow a response to be created once per event
    def test_func(self):
        event_id = self.kwargs.get('event')
        if Response.objects.filter(event=event_id).count() == 0:
            return True
        return False
    def form_valid(self, form):
        form.instance.account = self.request.user.account
        form.instance.event_id = self.kwargs.get('event')
        return super().form_valid(form)