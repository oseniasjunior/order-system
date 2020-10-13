from django_filters import filterset
from django_filters.widgets import BooleanWidget

from core import models


class MeansPaymentFilter(filterset.FilterSet):
    description = filterset.CharFilter(lookup_expr='icontains')
    active = filterset.BooleanFilter(widget=BooleanWidget)
    year = filterset.NumberFilter(field_name='created_at', lookup_expr='date__year')

    class Meta:
        model = models.MeansPayment
        fields = ['description', 'active', 'year']


class ProductFilter(filterset.FilterSet):
    active = filterset.BooleanFilter(widget=BooleanWidget)
    price_start = filterset.NumberFilter(field_name='sale_price', lookup_expr='gte')
    price_end = filterset.NumberFilter(field_name='sale_price', lookup_expr='lte')

    class Meta:
        model = models.Product
        fields = ['active', 'price_start', 'price_end']
