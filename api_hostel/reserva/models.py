from django.db import models
from api_hostel.funcionario.models import funcionario
from api_hostel.hospede.models import hospede
from api_hostel.quarto_cama.models import *

class reserva(models.Model):
    hospede = models.ForeignKey(hospede, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(funcionario, on_delete=models.CASCADE)
    

class status_reserva(models.Model):
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.descricao


class reserva_cama(models.Model):
    cama = models.ForeignKey(cama, on_delete=models.CASCADE)
    reserva = models.ForeignKey(reserva, on_delete=models.CASCADE)
    status_reserva = models.ForeignKey(status_reserva, on_delete=models.DO_NOTHING)
    inicio = models.DateField()
    fim = models.DateField()