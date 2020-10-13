from django.db.models import Q
from django_filters import filterset
from django_filters.widgets import BooleanWidget

from core import models


class NumberInFilter(filterset.BaseInFilter, filterset.NumberFilter):
    pass


class MeansPaymentFilter(filterset.FilterSet):
    description = filterset.CharFilter(lookup_expr='icontains')
    active = filterset.BooleanFilter(widget=BooleanWidget)
    year = filterset.NumberFilter(field_name='created_at', lookup_expr='date__year')

    class Meta:
        model = models.MeansPayment
        fields = ['description', 'active', 'year']


class ProductFilter(filterset.FilterSet):
    name_or_detail_description = filterset.CharFilter(method='filter_name_or_detail_description')
    active = filterset.BooleanFilter(widget=BooleanWidget)
    price_start = filterset.NumberFilter(field_name='sale_price', lookup_expr='gte')
    price_end = filterset.NumberFilter(field_name='sale_price', lookup_expr='lte')
    sale_price = NumberInFilter(lookup_expr='in')

    @staticmethod
    def filter_name_or_detail_description(queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(detail_description__icontains=value))

    class Meta:
        model = models.Product
        fields = ['active', 'price_start', 'price_end', 'sale_price', 'name_or_detail_description']
