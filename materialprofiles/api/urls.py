from django.urls import path

from .views import (MaterialProfileListCreateAPIView, MaterialDescriptionListCreateAPIView,
                    MaterialDescriptionRetrieveUpdateDestroyAPIView)

app_name = "material"

urlpatterns = [
    path('', MaterialProfileListCreateAPIView.as_view(), name='profile_list_create'),
    path('descriptions/', MaterialDescriptionListCreateAPIView.as_view(), name='descriptions_list_create'),
    path('descriptions/<int:pk>/', MaterialDescriptionRetrieveUpdateDestroyAPIView.as_view(), name='descriptions_retrieve_update_destroy'),
]
