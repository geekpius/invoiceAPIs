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
    user = serializers.StringRelatedField()

    class Meta:
        model = Activity
        exclude = ("id",)


class AuthUserSerializer(serializers.ModelSerializer):
    is_expired = serializers.SerializerMethodField()
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["email", "name", "last_login", "subscribe", 
        "expired_at", "is_expired", "activities", "created_at"]

    def get_is_expired(self, object):
        if not object.expired_at is None:
            return date.today() > object.expired_at
        return None


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Profile
        exclude = ("id",)

class ProfileAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["logo"]
