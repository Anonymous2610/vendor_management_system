from rest_framework.serializers import ModelSerializer
from .models import Vendor, PurchaseOrder

class VendorSerializer(ModelSerializer):

    class Meta:
        model = Vendor
        fields =['name' , 'contact_details','address','vendor_code']


class VendorPerformanceSerializer(ModelSerializer):

    class Meta:
        model = Vendor
        fields =['on_time_delivery_rate' , 'quality_rating_avg','average_response_time','fulfillment_rate']


class PurchaseOrderSerializer(ModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = '__all__'