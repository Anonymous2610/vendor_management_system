from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Vendor, PurchaseOrder

class VendorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor_data = {'name': 'Vendor A', 'contact_details': 'Contact A', 'address': 'Address A', 'vendor_code': 'V001'}
        self.vendor = Vendor.objects.create(**self.vendor_data)
        self.vendor_url = reverse('vendor-list-create')

    def test_create_vendor(self):
        unique_vendor_code = "VENDOR_123"
        self.vendor_data['vendor_code'] = unique_vendor_code
        response = self.client.post(self.vendor_url, self.vendor_data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_vendors(self):
        response = self.client.get(self.vendor_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests for other vendor endpoints (retrieve, update, delete)

class PurchaseOrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name='Vendor A', contact_details='Contact A', address='Address A', vendor_code='V001')
        self.purchase_order_data = {
            'po_number': 'PO001',
            'vendor': self.vendor.id,  # Use the primary key instead of the whole Vendor object
            'order_date': '2023-08-10',
            'items': {'item1': 5},
            'quantity': 5
        }
        self.purchase_order_url = reverse('purchase-order-list-create')

    def test_create_purchase_order(self):
        response = self.client.post(self.purchase_order_url, self.purchase_order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_purchase_orders(self):
        response = self.client.get(self.purchase_order_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests for other purchase order endpoints (retrieve, update, delete)

class VendorPerformanceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name='Vendor A', contact_details='Contact A', address='Address A', vendor_code='V001')
        self.vendor_performance_url = reverse('vendor-performance-retrieve', args=[self.vendor.id])

    def test_get_vendor_performance(self):
        response = self.client.get(self.vendor_performance_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests for vendor performance endpoint
