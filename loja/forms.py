from django import forms
from django.forms import ModelForm
from .models import Produto, Categoria


class ProdutoForm(ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()

    class Meta:
        model = Produto
        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria', 'required': True}),
            "valor": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': 0.10, 'required': True}),
            "categoria": forms.Select(attrs={'class': 'form-select', 'aria-label': 'Selecione', 'required': True})
        }
        fields = ['nome', 'valor', 'categoria']


class CategoriaForm(ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()

    class Meta:
        model = Categoria
        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria', 'required': True}),
        }
        fields = ['nome']
