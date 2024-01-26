from django.db import models

from account.models import User
from products.models import Products


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(max_length=12)
    color = models.CharField(max_length=20)
    quantity = models.SmallIntegerField()
    price = models.PositiveIntegerField()


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    fullname = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return self.user.phone


class DiscountCode(models.Model):
    discount_name = models.CharField(max_length=10, unique=True)
    discount_code = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.discount_name
