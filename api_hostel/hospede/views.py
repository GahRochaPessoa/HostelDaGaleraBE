from rest_framework import viewsets
from api_hostel.hospede.models import hospede
from api_hostel.hospede.serializers import *


class hospedesViewSet(viewsets.ModelViewSet):
    queryset = hospede.objects.all()
    serializer_class = HospedeSerializer
