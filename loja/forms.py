from django.forms import ModelForm
from .models import Produto, Categoria

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'valor', 'categoria']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']
