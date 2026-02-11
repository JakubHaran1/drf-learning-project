from rest_framework import serializers
from .models import ApartmentModel, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username"]


class ApartmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ApartmentModel
        fields = '__all__'
