from django.contrib import admin
from .models import Categoria, Produto, Carro

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Carro)
