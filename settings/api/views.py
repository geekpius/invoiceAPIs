from rest_framework import status
from rest_framework.generics import (RetrieveUpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import PercentageSerializer
from settings.models import Percentage
from core.permissions import IsOwnerOrReadOnly


class PercentageRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PercentageSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_object(self):
        return self.request.user.percentage


    