from tkinter import CASCADE
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

class Carro(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)

