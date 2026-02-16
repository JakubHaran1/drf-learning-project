from rest_framework import serializers
from .models import ApartmentModel, User


class ApartmentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ApartmentModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True)

    class Meta:
        model = User
        fields = ["username", 'apartments']

    def create(self, validated_data):
        apartments_data = validated_data.pop('apartments')
        user = User.objects.create(**validated_data)

        for data in apartments_data:
            ApartmentModel.objects.create(user=user, **data)

        return user
