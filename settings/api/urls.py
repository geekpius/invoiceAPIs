from django.urls import path

from .views import (PercentageRetrieveUpdateAPIView)

app_name = "settings"

urlpatterns = [
    path('percentages/', PercentageRetrieveUpdateAPIView.as_view(), name='percentage_retrieve_update'),
]
