from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('vendors/', views.VendorView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', views.VendorDetailView.as_view(), name='vendor-retrieve-update-delete'),
    path('purchase_orders/', views.PurchaseOrderView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderDetailView.as_view(), name='purchase-order-retrieve-update-delete'),
    path('vendors/<int:pk>/performance/', views.VendorPerformanceView.as_view(), name='vendor-performance-retrieve'),
    path('purchase_orders/<int:pk>/acknowledge/', views.AcknowledgeOrder.as_view({"post": "acknowledge"}), name='purchase-order-acknowledge'),
]
