# from django.db.models.signals import post_save
# from .models import Delivery, DeliveryStatusChoices
# from django.dispatch import receiver

# @receiver(post_save, sender=Delivery)
# def update_delivery_status(sender, instance, created, **kwargs):
#     if created:
#         instance.status = 'pending'
#         instance.save()
#         DeliveryStatusChoices.objects.create(status=instance.status)