# Generated by Django 5.0.2 on 2024-02-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb', '0002_homepageimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Id_number',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='Mpesa_code',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
