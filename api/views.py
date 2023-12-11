from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Vendor, PerformanceHistory, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer

class VendorView(ListCreateAPIView):
    """List all vendors or create a new one."""
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a vendor instance."""
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'pk'

class PurchaseOrderView(ListCreateAPIView):
    """List all purchase orders or create a new one."""
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetailView(RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a purchase order instance."""
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'pk'

class VendorPerformanceView(RetrieveAPIView):
    """Retrieve the performance metrics for a specific vendor."""
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'pk'

class AcknowledgeOrder(viewsets.ModelViewSet):
    """Acknowledge a purchase order."""
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'pk'

    @action(detail=True, methods=['POST'])
    def acknowledge(self, request, pk=None):
        """Acknowledge a purchase order."""
        purchase_order = self.get_object()
        purchase_order.acknowledge()
        return Response({'status': 'Acknowledged'}, status=status.HTTP_200_OK)
