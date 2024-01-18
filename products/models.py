from django.db import models


# Create your models here.


class Color(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    size = models.ManyToManyField(Size, blank=True, null=True, related_name="products_size")
    color = models.ManyToManyField(Color, related_name="products_image")

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="products_image", blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='image')

    def __str__(self):
        return self.product.title


class Informations(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='information')

    def __str__(self):
        return self.text
