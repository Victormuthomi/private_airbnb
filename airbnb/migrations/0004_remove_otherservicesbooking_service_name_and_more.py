# Generated by Django 5.0.2 on 2024-03-01 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb', '0003_customer_id_number_customer_mpesa_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherservicesbooking',
            name='service_name',
        ),
        migrations.DeleteModel(
            name='OtherService',
        ),
        migrations.DeleteModel(
            name='OtherServicesBooking',
        ),
    ]