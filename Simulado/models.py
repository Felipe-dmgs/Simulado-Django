from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Livro(models.Model):
    titulo = models.models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    

class Acervo(models.Model):
    livro.models.ManyToManyField("Simulado.Model", verbose_name=_("livro"))
    type.models.CharField(max_length=2, types=Type.choices, default=Type.DIGITAL, verbose_name="Tipo")
    
    class Type(models.TextChoices):
        DIGITAL = "DT"
        FISICO = "FS"
        
    class Category(models.IntegerChoices):
        GENERALIDADES_INFORMACAO = 0,_("000 - Generalidades e Informação: Obras gerais, enciclopédias, jornais e biblioteconomia.")
        FILOSOFIA_PSICOLOGIA = 100,_("100 - Filosofia e Psicologia: Ética, lógica e investigações sobre a mente humana.")
        RELIGIAO_TEOLOGIA = 200,_("200 - Religião e Teologia: Mitologia, teologia e estudos sobre crenças e religiões.")
        CIENCIAS_DIREITO = 300,_("300 - Ciências Sociais e Direito: Política, economia, sociologia, educação e leis.")
        LINGUISTICAS_IDIOMAS = 400,_("400 - Linguística e Idiomas: Gramáticas, dicionários e estudos de línguas.")
        CIENCIAS_PURAS = 500,_("500 – Ciências Puras (Exatas e Naturais): Matemática, física, química, biologia e astronomia.")
        CIENCIAS_APLICADAS = 600,_("600 – Ciências Aplicadas (Tecnologia): Medicina, engenharia, agricultura e administração.")
        ARTES_RECREACAO = 700,_("700 – Artes e Recreação: Pintura, música, arquitetura, esportes e lazer.")
        LITERATURA = 800,_("800 – Literatura: Poesia, romances, contos, crônicas e crítica literária.")
        HISTORIA_GEOGRAFIAM = 900,_("900 – História e Geografia: Biografias, viagens e acontecimentos históricos")