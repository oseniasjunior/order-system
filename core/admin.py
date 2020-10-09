from django.contrib import admin
from core import models, queries


# Register your models here.
@admin.register(models.MeansPayment)
class MeansPaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'modified_at', 'active']
    list_display_links = ['id', 'description', 'modified_at', 'active']
    search_fields = ['description']
    list_filter = ['active']
    list_per_page = 10


@admin.register(models.Table)
class TablePaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'modified_at', 'active']
    list_display_links = ['id', 'number', 'modified_at', 'active']
    search_fields = ['number']
    list_filter = ['active']
    list_per_page = 10


@admin.register(models.Product)
class ProductPaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sale_price', 'modified_at', 'active']
    list_display_links = ['id', 'name', 'sale_price', 'modified_at', 'active']
    search_fields = ['name', 'sale_price']
    list_filter = ['active']
    list_per_page = 10


class OrderItemInLine(admin.TabularInline):
    model = models.OrderItem
    extra = 1


class MeansPaymentOrderInLine(admin.TabularInline):
    model = models.MeansPaymentOrder
    extra = 1


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'table', 'user', 'status', 'modified_at', 'active']
    list_display_links = ['id', 'date', 'table', 'user', 'status', 'modified_at', 'active']
    search_fields = ['id', 'date', 'table', 'user']
    list_filter = ['active', 'status']
    list_per_page = 10
    inlines = [OrderItemInLine, MeansPaymentOrderInLine, ]


@admin.register(models.TotalOrderMeansPayment)
class TotalOrderMeansPaymentAdmin(admin.ModelAdmin):
    change_list_template = 'admin/total_order_means_payment.html'
    date_hierarchy = 'created_at'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        response.context_data['orders'] = list(queries.total_sale_by_means_payment())
        return response
