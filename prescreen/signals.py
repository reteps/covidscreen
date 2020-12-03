from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from django.contrib.auth.models import User

@receiver(post_save, sender=User) # emits signal when User is saved -> receiver
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

# Note that these ccould be combined but are seperated for clarity
@receiver(post_save, sender=User) # emits signal when User is saved -> receiver
def save_account(sender, instance, created, **kwargs):
    instance.account.save()