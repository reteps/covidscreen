from django.utils.translation import gettext_lazy as _
from prescreen.models import Response, Event
from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
# https://github.com/reteps/mozilla-django-tutorial/blob/master/catalog/forms.py
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['temperature', 'contact_with_covid']
        labels = {'contact_with_covid': 'Have you had contact with covid in the last 14 days?'}
        help_texts = {'temperature': 'Your temperature in degrees.'}

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}) # TODO improve solution to use a library for this
        }
    def clean_start_time(self):
        data = self.cleaned_data['start_time']
        if data < datetime.now():
            raise ValidationError(_('That date / time has already passed.'))
        return data
class EventJoinForm(forms.Form):
    code = forms.CharField(label='Event Code', max_length=100)
    
    def clean_code(self):
        data = self.cleaned_data['code']
        try:
            Event.objects.get(uuid=data)
            return data
            # alternative Event.objects.filter(uuid=data).count()
        except Event.DoesNotExist:
            raise ValidationError(_('An event with that code does not exist.'))