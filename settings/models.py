from django.conf import settings
from django.db import models


class Percentage (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="percentage", on_delete=models.CASCADE)
    vat = models.DecimalField(max_digits=60, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=60, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Metadata
    class Meta :
        ordering = ['pk']

    #Methods
    def __str__(self):
        return self.user
