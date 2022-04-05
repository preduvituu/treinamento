from django.shortcuts import redirect, render
from .models import Produto
from .forms import ProdutoForm

def listagem(request):
    produtos = Produto.objects.all()
    produtos_a_exibir = {
        'produtos': produtos
    }
    return render(request, 'listagem.html', produtos_a_exibir)

def cadastro_produto(request):
    formulario = {}
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_listagem")
    formulario['form'] = form
    return render(request, 'cadastro_produto.html', formulario)

def carrinho(request):
    return render(request, 'carrinho.html')

def detalhes(request):
    pass