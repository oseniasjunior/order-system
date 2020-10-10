from rest_framework import serializers
from core import models


class MeansPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MeansPayment
        fields = '__all__'
