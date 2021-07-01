from rest_framework import viewsets
from api_hostel.quarto_cama.models import *
from api_hostel.quarto_cama.serializers import *


class tipoquartoViewSet(viewsets.ModelViewSet):
    queryset = tipo_quarto.objects.all()
    serializer_class = TipoQuartoSerializer

class quartoViewSet(viewsets.ModelViewSet):
    queryset = quarto.objects.all()
    serializer_class = QuartoSerializer

class tipocamaViewSet(viewsets.ModelViewSet):
    queryset = tipo_cama.objects.all()
    serializer_class = TipoCamaSerializer

class camaViewSet(viewsets.ModelViewSet):
    queryset = cama.objects.all()
    serializer_class = CamaSerializer
