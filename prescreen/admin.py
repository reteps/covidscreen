from django.contrib import admin
from .models import Event, Account, QuestionSet, CovidScreenData, Response
# Register your models here.

admin.site.register(Event)
admin.site.register(Account)
admin.site.register(QuestionSet)
admin.site.register(CovidScreenData)
admin.site.register(Response)
