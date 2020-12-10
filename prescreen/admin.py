from django.contrib import admin
from prescreen.models import Event, CustomQuestionResponse, CustomQuestion, Response
# Register your models here.

class CustomQuestionsInline(admin.StackedInline):
    model = CustomQuestion
class CustomQuestionResponsesInline(admin.TabularInline):
    model = CustomQuestionResponse
# @admin.register(CovidScreenData)
# class CovidScreenDataAdmin(admin.ModelAdmin):
#     list_display = ('temperature', 'contact_with_covid')
#     inlines = [CustomQuestionResponsesInline]
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [CustomQuestionsInline]
    list_display = ('title', 'creator', 'num_responses', 'start_time')
@admin.register(CustomQuestion)
class CustomQuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'event', 'num_answers')
    inlines = [CustomQuestionResponsesInline]
@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'time')
    inlines = [CustomQuestionResponsesInline]
    fieldsets = (
        ('General Data', {
            'fields': ('account', 'time', 'event')
        }),
        ('COVID Form Data', {
            'classes': ('collapse',),
            'fields': ('temperature', 'contact_with_covid'),
        })
    )


@admin.register(CustomQuestionResponse)
class CustomQuestionResponseAdmin(admin.ModelAdmin):
    # pass
    fields = ('question', 'answer', 'response')
    # exclude
    list_display = ('question', 'answer', 'answered_by')