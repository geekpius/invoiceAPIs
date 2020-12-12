from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from core.permissions import IsOwnerOrReadOnly

from .serializers import (AuthUserSerializer, ProfileLogoSerializer,
                          ProfileSerializer, UserCreateSerializer)

  
# class UserCreateAPIView(APIView):
    
#     def post(self, request):
#         serializer = UserCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             response = {
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token),
#             }
#             return Response(response, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

    
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except expression as identifier:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthUserRetrieveAPIView(RetrieveUpdateAPIView):
    serializer_class = AuthUserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user


class ProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user.profile


class ProfileLogoUpdateAPIView(UpdateAPIView):
    serializer_class = ProfileLogoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


    