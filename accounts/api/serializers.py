from datetime import date

from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import Activity, Profile

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     "input_type":   "password"})

    class Meta:
        model = User
        fields = ["email", "name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Activity
        exclude = ("id",)


class AuthUserSerializer(serializers.ModelSerializer):
    is_expired = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["email", "name", "last_login", "subscribe", 
        "expired_at", "is_expired", "created_at"]

    def get_is_expired(self, instance):
        if not instance.expired_at is None:
            return date.today() > instance.expired_at
        return None

    def get_last_login(self, instance):
        return instance.last_login.strftime("%Y-%m-%d, %H:%M")


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    logo = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        exclude = ("id",)


class ProfileLogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["logo"]
