from django.contrib import admin
from .models import Event, Account, CovidScreen, CovidScreenInstance
# Register your models here.

admin.site.register(Event)
admin.site.register(Account)
admin.site.register(CovidScreen)
admin.site.register(CovidScreenInstance)
