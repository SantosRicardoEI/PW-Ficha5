from django.db import models


class PT(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Sessao(models.Model):
    pt = models.ForeignKey(PT, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    class Meta:
        unique_together = ('pt', 'data', 'hora')

    def __str__(self):
        return f"{self.cliente} - {self.pt} - {self.data} {self.hora}"