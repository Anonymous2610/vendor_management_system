from django.contrib import admin
from .models import Vendor,PerformanceHistory,PurchaseOrder
# Register your models here.
admin.site.register(Vendor)
admin.site.register(PerformanceHistory)
admin.site.register(PurchaseOrder)

