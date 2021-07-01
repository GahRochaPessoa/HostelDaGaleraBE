from rest_framework import serializers
from api_hostel.hospede.models import hospede

class HospedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = hospede
        fields = ('id','cpf','nome', 'email', 'telefone', 'data_nascimento')