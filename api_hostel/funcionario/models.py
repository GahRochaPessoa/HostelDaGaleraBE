from django.db import models


class tipo_funcionario(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome


class funcionario(models.Model):
    tipo_funcionario = models.ForeignKey(tipo_funcionario, on_delete=models.DO_NOTHING)
    cpf = models.CharField(max_length=15)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    telefone = models.CharField(max_length=15, null=True)
    data_nascimento = models.DateField()
<<<<<<< HEAD
    
    def __str__(self):
        return self.nome
=======

    def __str__ (self):
        return self.tipo_funcionario, self.cpf, self.nome, self.email, self.telefone, self.data_nascimento
>>>>>>> 506ca0e53c66e0103bb029371344008b7b590f55
