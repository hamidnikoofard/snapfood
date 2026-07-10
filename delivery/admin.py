from django.contrib import admin
from .models import Delivery, DeliveryStatusChoices


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'origin', 'destination',
                    'order_id', 'status', 'estimated_time']
    list_filter = ['status']
    search_fields = ['order_id']
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ['id', 'order_id']


admin.site.register(DeliveryStatusChoices)
