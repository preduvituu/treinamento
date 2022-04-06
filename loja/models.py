from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

class Carro(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)

