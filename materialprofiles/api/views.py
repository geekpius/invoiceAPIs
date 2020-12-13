from rest_framework import status
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from .serializers import MaterialProfileSerializer, MaterialDescriptionSerializer
from materialprofiles.models import MaterialProfile, MaterialDescription
from core.permissions import IsOwnerOrReadOnly, IsOwner


class MaterialProfileListCreateAPIView(ListCreateAPIView):
    serializer_class = MaterialProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = MaterialProfile.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        name = self.request.data["name"]
        if MaterialProfile.objects.filter(user=user, name=name).exists():
            raise ValidationError(f"{name} already exist.")
        serializer.save(user=user)


class MaterialDescriptionListCreateAPIView(ListCreateAPIView):
    serializer_class = MaterialDescriptionSerializer
    permission_classes = [IsAuthenticated]
    queryset = MaterialDescription.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class MaterialDescriptionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MaterialDescriptionSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = MaterialDescription.objects.all()


    