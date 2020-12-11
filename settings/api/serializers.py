from rest_framework import serializers

from settings.models import Percentage


class PercentageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Percentage
        exclude = ("id",)


