from django.core.exceptions import ValidationError
from django.db import models


class Artista(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    genero = models.CharField("género musical", max_length=50, blank=True)

    class Meta:
        ordering = ("nome",)

    def __str__(self):
        return self.nome


class Festival(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    data_inicio = models.DateField("data de início")
    data_fim = models.DateField("data de fim")
    artistas = models.ManyToManyField(Artista, related_name="festivais", blank=True)

    class Meta:
        ordering = ("data_inicio", "nome")

    def clean(self):
        if self.data_inicio and self.data_fim and self.data_fim < self.data_inicio:
            raise ValidationError(
                {"data_fim": "A data de fim não pode ser anterior à data de início."}
            )

    def __str__(self):
        return f"{self.nome} — {self.local}"


class Palco(models.Model):
    nome = models.CharField(max_length=100)
    festival = models.ForeignKey(
        Festival,
        on_delete=models.CASCADE,
        related_name="palcos",
    )

    class Meta:
        ordering = ("festival", "nome")
        constraints = [
            models.UniqueConstraint(
                fields=("festival", "nome"),
                name="palco_nome_unico_por_festival",
            )
        ]

    def __str__(self):
        return f"{self.nome} ({self.festival.nome})"

