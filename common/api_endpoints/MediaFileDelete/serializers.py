from rest_framework import serializers

from common.models import MediaFile


class MediaFileDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = [
            'file'
        ]