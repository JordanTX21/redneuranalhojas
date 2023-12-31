from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class ImageUploadSerializer(serializers.Serializer):
    file = serializers.ImageField()