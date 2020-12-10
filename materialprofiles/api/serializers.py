from rest_framework import serializers

from materialprofiles.models import MaterialProfile


class MaterialProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MaterialProfile
        exclude = ("id",)


