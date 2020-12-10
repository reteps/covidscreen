from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# https://stackoverflow.com/questions/43847173/cannot-import-models-from-another-app-in-django
class Account(models.Model):
    """ model for a user account """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(
        "prescreen.Event", blank=True
    )  # An account can have many events, and an event can belong to many accounts

    def __str__(self):
        return f"{self.user.username} Account"