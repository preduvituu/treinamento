from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import CategoriaForm, ProdutoForm
from .models import Produto, Carro
from django.db.models import Sum

def listagem(request):
    context = {}
    context['produtos'] = Produto.objects.all()
    return render(request, 'listagem.html', context)


def cadastroCategoria(request):
    formulario = {}
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("listagem")
    formulario['form'] = form
    return render(request, 'cadastro_categoria.html', formulario)
    

def cadastroProduto(request):
    context = {}
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("listagem")
    context['form'] = form
    return render(request, 'cadastro_produto.html', context)


def carrinho(request, pk_produto):

    if True if request.GET.get('add') == 'True' else False:
        produto = Produto.objects.get(id=pk_produto)
        carro = Carro.objects.update_or_create(produto=produto)
        return redirect(reverse('carrinho', args=[carro[0].id]))

    context = {}
    context['carrinho'] = Carro.objects.all()
    context['valor_total'] = Carro.objects.all().aggregate(Sum('produto__valor'))
    return render(request, 'carrinho.html', context)


def detalhes(request, pk):
    context = {}
    context['produto'] = get_object_or_404(Produto, pk=pk)
    return render(request, 'detalhes.html', context)


def comprarCarrinho(request):
    produtos_carro = Carro.objects.all()
    for produto in produtos_carro:
        produto.produto.vendido = True
        produto.produto.save()
    return redirect('listagem')
