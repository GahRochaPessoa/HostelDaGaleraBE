from rest_framework import serializers
from api_hostel.pagamento.models import *

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pagamento
        fields = ('id', 'reserva', 'forma_pagamento', 'valor_total')