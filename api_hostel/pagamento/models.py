from django.db import models
from api_hostel.reserva.models import reserva

class pagamento(models.Model):
    reserva = models.ForeignKey(reserva, on_delete=models.CASCADE)
    forma_pagamento = models.CharField(max_length=100)
    valor_total = models.FloatField()