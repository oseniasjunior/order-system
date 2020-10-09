from django.contrib import admin
from core import models


# Register your models here.
@admin.register(models.MeansPayment)
class MeansPayment(admin.ModelAdmin):
    list_display = ['id', 'description', 'modified_at', 'active']
    list_display_links = ['id', 'description', 'modified_at', 'active']
    search_fields = ['description']
    list_filter = ['active']
    list_per_page = 10


@admin.register(models.Table)
class TablePayment(admin.ModelAdmin):
    list_display = ['id', 'number', 'modified_at', 'active']
    list_display_links = ['id', 'number', 'modified_at', 'active']
    search_fields = ['number']
    list_filter = ['active']
    list_per_page = 10


@admin.register(models.Product)
class ProductPayment(admin.ModelAdmin):
    list_display = ['id', 'name', 'sale_price', 'modified_at', 'active']
    list_display_links = ['id', 'name', 'sale_price', 'modified_at', 'active']
    search_fields = ['name', 'sale_price']
    list_filter = ['active']
    list_per_page = 10
