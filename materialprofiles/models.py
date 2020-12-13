from django.conf import settings
from django.db import models


class MaterialProfile (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="materialprofiles", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Metadata
    class Meta :
        ordering = ['name']

    #Methods
    def __str__(self):
        return self.name


class MaterialDescription (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="materialdescriptions", on_delete=models.CASCADE)
    profile = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=60, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Metadata
    class Meta :
        ordering = ['pk']

    #Methods
    def __str__(self):
        return self.profile

