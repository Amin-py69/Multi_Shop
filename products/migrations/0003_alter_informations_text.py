# Generated by Django 5.0.1 on 2024-01-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_informations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informations',
            name='text',
            field=models.TextField(),
        ),
    ]
