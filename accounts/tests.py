from datetime import date, datetime, timedelta

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User

# User = get_user_model()


class AccountTestCase(APITestCase):
    def setUp(self):
        User = get_user_model()
        User.objects.create_user(email='admin@gmail.com', name="Fiifi Pius", password='aaaaaa')
        User.objects.create_user(email="fiifipius@gmail.com", name="Fiifi Pius", password="aaaaaa")
        User.objects.create_user(email="fiifijava@gmail.com", name="Fiifi Java", password="aaaaaa")

        #get token
        user = User.objects.create_user(email="my@gmail.com", name="Fiifi Java", password="aaaaaa")
        client = APIClient()
        refresh = RefreshToken.for_user(user)
        # self.token = client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        self.token = refresh.access_token

    def test_is_expired(self):
        user = User.objects.get(email="fiifipius@gmail.com")
        is_expired = date.today() > user.expired_at
        self.assertTrue(True, is_expired)

    def test_is_not_expired(self):
        user = User.objects.get(email="fiifijava@gmail.com")
        is_expired = date.today() > user.expired_at
        self.assertFalse(False, is_expired)

    def test_auth_token(self):
        credentials = {
            "email": "admin@gmail.com",
            "password": "aaaaaa"
        }
        url = reverse("auth:token_obtain_pair") 
        client = APIClient()
        response = client.post(url, credentials)
        self.assertTrue(response.status_code == status.HTTP_200_OK)

    def test_not_auth_token(self):
        credentials = {
            "email": "fiifi@gmail.com",
            "password": "aaaaaa"
        }
        url = reverse("auth:token_obtain_pair") 
        client = APIClient()
        response = client.post(url, credentials)
        self.assertTrue(response.status_code == status.HTTP_401_UNAUTHORIZED)
    
    def test_register(self):
        data = {
            "email": "fiifi@gmail.com",
            "name": "Fiifi Pius",
            "password": "aaaaaa"
        }
        url = reverse("auth:register") 
        client = APIClient()
        response = client.post(url, data)
        self.assertTrue(response.status_code == status.HTTP_201_CREATED)

    def test_get_auth_user(self):
        url = reverse("auth:user_retrieve_update")
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = client.get(url)
        self.assertTrue(response.status_code == status.HTTP_200_OK)

    def test_update_auth_user(self):
        url = reverse("auth:user_retrieve_update")
        client = APIClient()
        info = {
            "email": "my@gmail.com", 
            "name": "Fiifi J"
        }
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = client.put(url, info)
        self.assertTrue(response.status_code == status.HTTP_200_OK)