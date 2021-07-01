from rest_framework import serializers
from api_hostel.quarto_cama.models import *

class TipoQuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_quarto
        fields = ('id','nome')

class QuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = quarto 
        fields = ('id','tipo_quarto', 'nome', 'descricao')

class TipoCamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_cama
        fields = ('id','nome')

class CamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = cama
        fields = ('id','tipo_cama','quarto','status','nome','descricao','valor')