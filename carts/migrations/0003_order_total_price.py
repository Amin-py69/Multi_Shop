# Generated by Django 5.0.1 on 2024-01-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_remove_order_address_remove_order_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
