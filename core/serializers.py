from rest_framework import serializers
from core import models


class MeansPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MeansPayment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
