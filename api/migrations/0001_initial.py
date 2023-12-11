# Generated by Django 4.2.8 on 2023-12-05 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contact_details', models.TextField(max_length=30)),
                ('address', models.TextField(max_length=50)),
                ('vendor_code', models.CharField(max_length=10, unique=True)),
                ('on_time_delivery_rate', models.FloatField(default=100.0)),
                ('quality_rating_avg', models.FloatField(default=5.0)),
                ('average_response_time', models.FloatField(blank=True)),
                ('fulfillment_rate', models.FloatField(default=100.0)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=10, unique=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('completed', 'COMPLETED'), ('canceled', 'CANCELED')], default='pending', max_length=15)),
                ('quality_rating', models.FloatField(default=0)),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('acknowledgment_date', models.DateTimeField(null=True)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.vendor')),
            ],
        ),
    ]