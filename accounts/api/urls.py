from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (AuthUserRetrieveAPIView, LogoutAPIView,
                    ProfileLogoUpdateAPIView, ProfileRetrieveUpdateAPIView,
                    UserCreateAPIView)

app_name = "auth"

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', AuthUserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('profile/', ProfileRetrieveUpdateAPIView.as_view(), name='profile_retrieve'),
    path('profile-logo/', ProfileLogoUpdateAPIView.as_view(), name='profile_logo_update'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
