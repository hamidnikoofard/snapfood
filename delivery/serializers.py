from rest_framework import serializers
from .models import Delivery, DeliveryStatusChoices
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class DeliverySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    # user = UserSerializer(read_only=True)
    status = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryCreateSerializer(serializers.ModelSerializer):
    estimated_time = serializers.IntegerField(read_only=True)

    class Meta:
        model = Delivery
        fields = ['origin', 'destination', 'order_id', 'estimated_time']


class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatusChoices
        fields = '__all__'
