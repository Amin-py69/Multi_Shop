# Generated by Django 5.0.1 on 2024-01-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_registerotp'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerotp',
            name='token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
