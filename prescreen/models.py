from django.db import models
from django.urls import reverse  # generate URLs by reversing URL patterns
import uuid
from users.models import Account

class Event(models.Model):
    """ model for an event """

    creator = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="Enter a title for this event")
    start_time = models.DateTimeField()
    # TODO Figure out shorter ID than uuid without collisions
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this event across whole system",
    )

    def num_responses(self):
        return Response.objects.filter(event=self.uuid).count()

    num_responses.short_description = "Number of Responses"

    def __str__(self):
        return f"{self.title} ({self.uuid})"
    def get_absolute_url(self):
        ''' return url to access event detail page'''
        return reverse('event-detail', args=[str(self.uuid)])

class CustomQuestion(models.Model):
    text = models.CharField(max_length=200)
    event = models.ForeignKey("Event", on_delete=models.SET_NULL, null=True)

    def num_answers(self):
        return CustomQuestionResponse.objects.filter(question=self.id).count()

    num_answers.short_description = "Number of Answers"

    def __str__(self):
        return f"{self.text}"


class CustomQuestionResponse(models.Model):
    question = models.ForeignKey("CustomQuestion", on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, blank=True)
    response = models.ForeignKey("Response", on_delete=models.SET_NULL, null=True)
    response.short_description = "Answered as a part of"

    def answered_by(self):
        return self.response.account.user.username

    answered_by.short_description = "Answered By"

    def __str__(self):
        return f"{self.question.text} - {self.response}"


class Response(models.Model):
    """ model for a completed covid screen """

    temperature = models.DecimalField(max_digits=5, decimal_places=2, default=98.6)
    contact_with_covid = models.BooleanField(default=False)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField()
    event = models.ForeignKey("Event", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account.user.username}\'s response for "{self.event.title}"'