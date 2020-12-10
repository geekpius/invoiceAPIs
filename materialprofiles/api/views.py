from rest_framework import status
from rest_framework.generics import (ListCreateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MaterialProfileSerializer
from materialprofiles.models import MaterialProfile
from core.permissions import IsOwnerOrReadOnly


class MaterialProfileListCreateAPIView(ListCreateAPIView):
    serializer_class = MaterialProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = MaterialProfile.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


    