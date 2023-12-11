from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor

@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, created, **kwargs):
    """Update the average response time for the vendor."""
    if not created and instance.acknowledgment_date:
        vendor = instance.vendor
        total_response_time = 0

        acknowledged_pos = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
        for po in acknowledged_pos:
            total_response_time += (po.acknowledgment_date - po.issue_date).total_seconds()

        vendor.average_response_time = total_response_time / acknowledged_pos.count()
        vendor.save()
