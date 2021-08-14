from rest_framework import viewsets
from api_hostel.pagamento.models import *
from api_hostel.pagamento.serializers import *


class pagamentoViewSet(viewsets.ModelViewSet):
    queryset = pagamento.objects.all()
    serializer_class = PagamentoSerializer
