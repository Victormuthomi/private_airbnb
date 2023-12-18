# Generated by Django 4.2.7 on 2023-11-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb', '0007_alter_booking_booking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='airbnb',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]
