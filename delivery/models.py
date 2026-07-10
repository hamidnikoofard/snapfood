from django.db import models
from django.contrib.auth.models import User


class DeliveryStatusChoices(models.Model):
    status = models.CharField(max_length=255, choices=[('pending', 'Pending'), (
        'in_progress', 'In Progress'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')]
    )

    def __str__(self):
        return self.status


class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(DeliveryStatusChoices, on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    estimated_time = models.IntegerField()

    def __str__(self):
        return self.order_id
