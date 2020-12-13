from rest_framework import serializers

from materialprofiles.models import MaterialProfile, MaterialDescription


class MaterialProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MaterialProfile
        exclude = ("id",)


class MaterialDescriptionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MaterialDescription
        exclude = ("id",)


