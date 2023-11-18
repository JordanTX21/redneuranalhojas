from rest_framework import serializers
from .models import Hoja
from django.contrib.auth.models import User


class HojaSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Hoja
        fields = ('id', 'title', 'genre', 'year', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    hojas = serializers.PrimaryKeyRelatedField(many=True, queryset=Hoja.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'hojas')
