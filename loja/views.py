from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from .forms import CategoriaForm, ProdutoForm
from .models import Produto, Carro


def cadastro_categoria(request):
    formulario = {}
    form = CategoriaForm(request.POST or None)
    if form.is_valid():dutos_ca= form
    return render(request, 'cadastro_categoria.html', formulario)

def cadastro_produto(request):
    formulario = {}
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        # import pdb; pdb.set_trace()
        form.save()
        return redirect("listagem")
    formulario['form'] = form
    return render(request, 'cadastro_produto.html', formulario)

def carrinho(request):
    if 'produto_id' in request.GET:
        produto = Produto.objects.get(id=int(request.GET.get('produto_id')))
        Carro.objects.create(
            produto=produto
        )
    produtos_carrinho = {
        'carrinho': Carro.objects.all()
    }
    return render(request, 'carrinho.html', produtos_carrinho)

def detalhes(request, produto_id):
    produtos = get_object_or_404(Produto, pk=produto_id)
    produtos_a_exibir = {
        'produtos': produtos
    }
    return render(request, 'detalhes.html', produtos_a_exibir)

def listagem(request):
    produtos_carro = Carro.objects.all()
    produtos = Produto.objects.filter(id__in=list(produtos_carro.values_list('produto_id', flat=True)))
    dados = {
        'produtos': produtos
    }
    return render(request, 'listagem.html', dados)
