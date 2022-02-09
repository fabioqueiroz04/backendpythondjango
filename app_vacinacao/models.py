from django.db import models

class Enfermeiro(models.Model):
    nome_enfermeiro = models.CharField(max_length=50)
    nome_vacina = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_vacina

class Gestor(models.Model):
    nome_gestor = models.CharField(max_length=50)
    nome_vacinados = models.CharField(max_length=50)
    escolha_vacina = models.OneToOneField(
        Enfermeiro,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.nome_gestor
