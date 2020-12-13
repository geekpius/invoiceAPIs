from django.urls import path

from .views import (MaterialProfileListCreateAPIView, MaterialDescriptionListCreateAPIView)

app_name = "material"

urlpatterns = [
    path('', MaterialProfileListCreateAPIView.as_view(), name='profile_list_create'),
    path('descriptions/', MaterialDescriptionListCreateAPIView.as_view(), name='descriptions_list_create'),
]
