from django_filters import filterset
from django_filters.widgets import BooleanWidget

from core import models


class MeansPaymentFilter(filterset.FilterSet):
    description = filterset.CharFilter(lookup_expr='icontains')
    active = filterset.BooleanFilter(widget=BooleanWidget)

    class Meta:
        model = models.MeansPayment
        fields = ['description', 'active']