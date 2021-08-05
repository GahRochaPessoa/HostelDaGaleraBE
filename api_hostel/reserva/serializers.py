from rest_framework import serializers
from api_hostel.reserva.models import *

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = reserva
        fields = ('id','hospede','funcionario')

class StatusReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = status_reserva 
        fields = ('id', 'descricao')

class ReservaCamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = reserva_cama
        fields = ('id','cama', 'reserva', 'status_reserva', 'inicio', 'fim')