from django.db import models
from django.contrib.auth.models import User
import uuid

class Account(models.Model):
    ''' model for a user account '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.ManyToManyField('Event', blank=True)
    def __str__(self):
        return f'{self.user.username} Account'
class Event(models.Model):
    ''' model for an event '''
    creator = models.ForeignKey("Account", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="Enter a title for this event")
    start_time = models.DateTimeField()
    # TODO Figure out shorter ID than uuid without collisions
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this event across whole system')
    custom_questions = models.ForeignKey('QuestionSet', on_delete=models.CASCADE, null=True)

    # covid_screen_options = models.ForeignKey('CovidScreenOptions', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title} {self.uuid}'
class QuestionSet(models.Model):
    ''' model representing the custom questions of a covid screen '''
    # TODO Figure out customization / optional questions
    # Do I just make slots for questions that could be asked?
    question_1 = models.CharField(max_length=200, blank=True)
    question_2 = models.CharField(max_length=200, blank=True)
    question_3 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return f'Covid Screen Questions ({self.question_1})'
    
class CovidScreenData(models.Model):
    custom_responses = models.ForeignKey('QuestionSet', on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, default=98.6)
    contact_with_covid = models.BooleanField(default=False)

class Response(models.Model):
    ''' model for a completed covid screen '''
    # TODO should this be a uuid for security reasons instead?
    account = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField()
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    details = models.ForeignKey('CovidScreenData', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.account.user.username}\'s Response ({self.event.title})'