from rest_framework import viewsets
from api_hostel.reserva.models import *
from api_hostel.reserva.serializers import *


class reservaViewSet(viewsets.ModelViewSet):
    queryset = reserva.objects.all()
    serializer_class = ReservaSerializer

class statusreservaViewSet(viewsets.ModelViewSet):
    queryset = status_reserva.objects.all()
    serializer_class = StatusReservaSerializer

class reservacamaViewSet(viewsets.ModelViewSet):
    queryset = reserva_cama.objects.all()
    serializer_class = ReservaCamaSerializer

