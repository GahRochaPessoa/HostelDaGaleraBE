from django.db import models


class tipo_quarto(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome


class quarto(models.Model):
    tipo_quarto = models.ForeignKey(tipo_quarto, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class tipo_cama(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class cama(models.Model):

    status_cama = (
        ('l','Livre'),
        ('o','Ocupada'),
    )

    tipo_cama = models.ForeignKey(tipo_cama, on_delete=models.DO_NOTHING)
    quarto = models.ForeignKey(quarto, on_delete=models.CASCADE)
    status = models.CharField(max_length=1,choices=status_cama)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
