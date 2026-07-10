from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .models import Delivery, DeliveryStatusChoices
from .serializers import DeliverySerializer, DeliveryCreateSerializer, UserSerializer
from .services import get_estimated_time_minutes


class DeliveryListCreateView(generics.ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeliveryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeliveryCreateView(generics.CreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliveryCreateSerializer

    def perform_create(self, serializer):
        self.origin = self.request.data.get('origin')
        self.destination = self.request.data.get('destination')

        try:
            estimated_time = get_estimated_time_minutes(
                self.origin,
                self.destination,
            )
        except ValueError as exc:
            raise ValidationError({'detail': str(exc)}) from exc

        status_obj, _ = DeliveryStatusChoices.objects.get_or_create(
            status='pending',
        )
        serializer.save(status=status_obj, estimated_time=estimated_time)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
