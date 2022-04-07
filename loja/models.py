from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    vendido = models.BooleanField(default=False)

class Carro(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.DO_NOTHING, related_name="produto_carro")

