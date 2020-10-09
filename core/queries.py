from core import models
from django.db.models import F, Sum


def total_sale_by_means_payment():
    queryset = models.MeansPaymentOrder.objects.select_related('means_payment').values(
        'means_payment__description'
    ).annotate(
        total=Sum('value')
    )
    print(queryset.query)
    return queryset
