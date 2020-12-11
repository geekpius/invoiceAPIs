from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch  import receiver
from .models import Percentage

User = get_user_model()


@receiver(post_save, sender=User)
def create_percentage(sender, instance, created, **kwargs):
    if created:
        Percentage.objects.create(user=instance)