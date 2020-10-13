from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core import models, serializers, filters


class MeansPaymentViewSet(viewsets.ModelViewSet):
    queryset = models.MeansPayment.objects.all()
    serializer_class = serializers.MeansPaymentSerializer
    filter_class = filters.MeansPaymentFilter
    ordering_fields = '__all__'
    ordering = ('-id',)

    # @action(methods=['GET'], detail=False)
    # def get_by_description(self, request, *args, **kwargs):
    #     params = request.query_params
    #     if 'description' in params:
    #         self.queryset = self.queryset.filter(description__icontains=params['description'])
    #         return super(MeansPaymentViewSet, self).list(request, *args, **kwargs)
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_class = filters.ProductFilter
    ordering_fields = '__all__'
    ordering = ('-id',)
