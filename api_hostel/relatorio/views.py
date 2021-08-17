from rest_framework import viewsets
from datetime import date
from django.http import JsonResponse
from api_hostel.reserva.models import *
from api_hostel.reserva.serializers import *
from api_hostel.pagamento.models import *
from api_hostel.pagamento.serializers import *

def relatorioOcupacao(request):
    dataini = request.GET.get('inicio')
    datafim = request.GET.get('fim')
    if dataini:
        if datafim:
            realizadas = reserva_cama.objects.filter(status_reserva__descricao__icontains='realizada',inicio__range=[dataini,datafim]).count()
            solicitadas = reserva_cama.objects.filter(status_reserva__descricao__icontains='solicitada',inicio__range=[dataini,datafim]).count()
            canceladas = reserva_cama.objects.filter(status_reserva__descricao__icontains='cancelada',inicio__range=[dataini,datafim]).count()
        else:
            realizadas = reserva_cama.objects.filter(status_reserva__descricao__icontains='realizada',inicio__range=[dataini,date.today()]).count()
            solicitadas = reserva_cama.objects.filter(status_reserva__descricao__icontains='solicitada',inicio__range=[dataini,date.today()]).count()
            canceladas = reserva_cama.objects.filter(status_reserva__descricao__icontains='cancelada',inicio__range=[dataini,date.today()]).count()
    else:
        realizadas = reserva_cama.objects.filter(status_reserva__descricao__icontains='realizada').count()
        solicitadas = reserva_cama.objects.filter(status_reserva__descricao__icontains='solicitada').count()
        canceladas = reserva_cama.objects.filter(status_reserva__descricao__icontains='cancelada').count()
    
    data = {
        'realizadas':realizadas,
        'solicitadas':solicitadas,
        'canceladas':canceladas
    }
    return JsonResponse(data)