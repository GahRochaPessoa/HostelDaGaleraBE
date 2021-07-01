from django.db import models

class hospede(models.Model):

    cpf = models.CharField(max_length=15)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    telefone = models.CharField(max_length=15, null=True)
    data_nascimento = models.DateField()
