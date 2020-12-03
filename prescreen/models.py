from django.db import models
from django.contrib.auth.models import User
import uuid

class Account(models.Model):
    ''' model for a user account '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.ManyToManyField('Event', blank=True) # An account can have many events, and an event can belong to many accounts
    def __str__(self):
        return f'{self.user.username} Account'
class Event(models.Model):
    ''' model for an event '''
    creator = models.ForeignKey("Account", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="Enter a title for this event")
    start_time = models.DateTimeField()
    # TODO Figure out shorter ID than uuid without collisions
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this event across whole system')
    # custom_questions = models.ManyToManyField(CustomQuestion) # A event can have many questions, but the questions 
    def num_responses(self):
        return Response.objects.filter(event=self.uuid).count()
    num_responses.short_description = 'Number of Responses'
    # covid_screen_options = models.ForeignKey('CovidScreenOptions', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title} ({self.uuid})'

class CustomQuestion(models.Model):
    text = models.CharField(max_length=200)
    event = models.ForeignKey("Event", on_delete=models.SET_NULL, null=True) # TODO I am confused
    def num_answers(self):
        return CustomQuestionResponse.objects.filter(question=self.id).count()
    num_answers.short_description = 'Number of Answers'
    def __str__(self):
        return f'{self.text}'
class CustomQuestionResponse(models.Model):
    question = models.ForeignKey('CustomQuestion', on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, blank=True)
    response = models.ForeignKey("Response", on_delete=models.SET_NULL, null=True) # TODO I am confused
    response.short_description = 'Answered as a part of'
    # @property # Allows '.answered_by' access
    def answered_by(self):
        return self.response.account.user.username
    answered_by.short_description = 'Answered By'
    def __str__(self):
         return f'{self.question.text} - {self.response}'
# class CovidScreenData(models.Model):
    # custom_responses = models.ManyToManyField(CustomQuestion) # TODO I am confused

class Response(models.Model):
    ''' model for a completed covid screen '''
    # TODO should this be a uuid for security reasons instead?
    temperature = models.DecimalField(max_digits=5, decimal_places=2, default=98.6)
    contact_with_covid = models.BooleanField(default=False)
    # details = models.OneToOneField('CovidScreenData', on_delete=models.CASCADE)
    account = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField()
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.account.user.username}\'s response for "{self.event.title}"'