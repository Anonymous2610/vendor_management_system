from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Vendor(models.Model):
    """
    Model to store information about vendors and their performance metrics.
    """

    name = models.CharField(max_length=255, blank=False)
    contact_details = models.TextField(max_length=100, blank=False)
    address = models.TextField(max_length=255, blank=False)
    vendor_code = models.CharField(max_length=10, unique=True, blank=False)
    on_time_delivery_rate = models.FloatField(default=0.0, null=True)
    quality_rating_avg = models.FloatField(default=0.0, null=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    """
    Model to track purchase orders and calculate various performance metrics.
    """

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ]

    po_number = models.CharField(max_length=10, unique=True, blank=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)
    items = models.JSONField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default='pending')
    quality_rating = models.FloatField(default=0)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

    def acknowledge(self):
        """
        Method to acknowledge a purchase order and update acknowledgment_date.
        """
        self.acknowledgment_date = datetime.now()
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the save method to update vendor metrics on saving a purchase order.
        """
        vendor_obj = self.vendor
        orders = PurchaseOrder.objects.filter(vendor=self.vendor.id)
        total_order = orders.count()
        if total_order!=0:
            fullfilled_orders = orders.filter(status='completed')
            total_completed_order = fullfilled_orders.count()
            
            if self.status == 'completed':
                vendor_obj.fulfillment_rate = (total_completed_order + 1) * 100 / (total_order + 1)
                today = datetime.now().date()
                cur_delivery_rate = (vendor_obj.on_time_delivery_rate / 100)

                if today <= self.delivery_date:
                    self.delivery_date = today
                    total_ontime = (cur_delivery_rate * total_completed_order + 1)
                    vendor_obj.on_time_delivery_rate = total_ontime * 100 / (total_completed_order + 1)
                    vendor_obj.save()
                else:
                    total_ontime = (cur_delivery_rate * total_completed_order)
                    vendor_obj.on_time_delivery_rate = total_ontime * 100 / (total_completed_order + 1)

                if self.quality_rating > 0:
                    total_rated = fullfilled_orders.filter(quality_rating__gt=0.0)
                    total_count = total_rated.count()
                    val = (total_count * vendor_obj.quality_rating_avg + self.quality_rating) / (total_count + 1)
                    vendor_obj.quality_rating_avg = val
            else:
                vendor_obj.fulfillment_rate = total_completed_order * 100 / (total_order)

            vendor_obj.save()
        super().save(*args, **kwargs)

class PerformanceHistory(models.Model):
    """
    Model to store historical data on vendor performance for trend analysis.
    """

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        name = self.vendor.name
        return f"Performance History of {name}"
