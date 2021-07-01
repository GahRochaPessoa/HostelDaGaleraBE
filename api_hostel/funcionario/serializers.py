from rest_framework import serializers
from api_hostel.funcionario.models import *

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = funcionario
        fields = ('id','tipo_funcionario','cpf','nome', 'email', 'telefone', 'data_nascimento')

class TipoFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_funcionario
        fields = ('id','nome')
