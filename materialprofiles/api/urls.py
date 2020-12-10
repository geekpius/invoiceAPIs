from django.urls import path

from .views import (MaterialProfileListCreateAPIView)

app_name = "material"

urlpatterns = [
    path('', MaterialProfileListCreateAPIView.as_view(), name='profile_list_create'),
]
