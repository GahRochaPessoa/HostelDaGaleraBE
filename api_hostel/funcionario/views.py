from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from api_hostel.funcionario.models import funcionario, tipo_funcionario
from api_hostel.funcionario.serializers import *


class funcionarioViewSet(viewsets.ModelViewSet):
    queryset = funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    
class tipofuncionarioViewSet(viewsets.ModelViewSet):
    queryset = tipo_funcionario.objects.all()
    serializer_class = TipoFuncionarioSerializer