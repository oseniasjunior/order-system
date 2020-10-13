from django.db import models
from django.db.models import ExpressionWrapper, F, FloatField, Sum, OuterRef, Subquery
from core import models as core_models


class MeansPaymentOrderQuerySet(models.QuerySet):
    def total_sale_by_means_payment(self):
        queryset = self.select_related('means_payment').values(
            'means_payment__description',
        ).annotate(
            total=Sum('value')
        ).values('means_payment__description', 'total')
        print(queryset.query)
        return queryset


class OrderItemQuerySet(models.QuerySet):
    def total_sale_by_product(self):
        queryset = self.select_related('product').annotate(
            subtotal=ExpressionWrapper(F('quantity') * F('unit_price'), output_field=FloatField())
        ).values('product__name').annotate(
            total=Sum('subtotal', output_field=FloatField())
        ).values('product__name', 'total')
        print(queryset.query)
        return queryset

    def total_sale_by_table(self):
        queryset = self.select_related('order', 'order__table').annotate(
            subtotal=ExpressionWrapper(F('quantity') * F('unit_price'), output_field=FloatField())
        ).values('order__table__number').annotate(
            total=Sum('subtotal', output_field=FloatField())
        ).values('order__table__number', 'total')

        return queryset


class ProductQuerySet(models.QuerySet):
    def last_sale(self):
        subquery = core_models.OrderItem.objects.select_related('order').filter(
            product=OuterRef('id')
        ).order_by('-order__date')

        queryset = self.annotate(
            last_sale=Subquery(subquery.values('order__date')[:1])
        ).values('id', 'name', 'last_sale')

        print(queryset.query)

        return queryset
