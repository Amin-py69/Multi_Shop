from django.contrib import admin
from . import models


# Register your models here.


class InformationAdmin(admin.StackedInline):
    model = models.Informations


class ImageAdmin(admin.StackedInline):
    model = models.Image


@admin.register(models.Products)
class Product(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']
    inlines = (InformationAdmin, ImageAdmin)


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Color)
admin.site.register(models.Size)
