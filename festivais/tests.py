from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Artista, Festival, Palco


class FestivalModelsTests(TestCase):
    def setUp(self):
        self.festival = Festival.objects.create(
            nome="Festival de Verão",
            local="Lisboa",
            data_inicio=date(2026, 7, 10),
            data_fim=date(2026, 7, 12),
        )

    def test_relacoes_do_festival(self):
        artista = Artista.objects.create(nome="Banda Exemplo", genero="Rock")
        palco = Palco.objects.create(nome="Palco Principal", festival=self.festival)
        self.festival.artistas.add(artista)

        self.assertIn(artista, self.festival.artistas.all())
        self.assertIn(self.festival, artista.festivais.all())
        self.assertIn(palco, self.festival.palcos.all())

    def test_data_final_anterior_a_inicial_e_invalida(self):
        festival = Festival(
            nome="Festival Inválido",
            local="Porto",
            data_inicio=date(2026, 8, 10),
            data_fim=date(2026, 8, 9),
        )

        with self.assertRaises(ValidationError):
            festival.full_clean()

    def test_nome_do_palco_e_unico_dentro_do_festival(self):
        Palco.objects.create(nome="Palco Principal", festival=self.festival)
        palco_repetido = Palco(nome="Palco Principal", festival=self.festival)

        with self.assertRaises(ValidationError):
            palco_repetido.full_clean()

