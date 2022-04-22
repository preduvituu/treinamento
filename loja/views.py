from django.shortcuts import get_object_or_404, redirect, render
from .forms import CategoriaForm, ProdutoForm
from .models import Produto, Carro
from django.contrib import messages

def listagem(request):
    if request.user.is_authenticated:
        produtos = Produto.objects.all()
        produtos_a_exibir = {
            'produtos': produtos
        }
        messages.success(request, 'Login feito com sucesso!')
        return render(request, 'listagem.html', produtos_a_exibir)
    else:
        redirect('login')

def cadastro_categoria(request):
    formulario = {}
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("listagem")
    formulario['form'] = form
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
    soma = 0
    for c in Carro.objects.all():
        soma += c.produto.valor

    produtos_carrinho = {
        'carrinho': Carro.objects.all(), 'soma':soma
        }
    return render(request, 'carrinho.html', produtos_carrinho)

def detalhes(request, produto_id):
    produtos = get_object_or_404(Produto, pk=produto_id)
    produtos_a_exibir = {
        'produtos': produtos
    }
    return render(request, 'detalhes.html', produtos_a_exibir)

def update(request):
    produtos_carro = Carro.objects.all()
    produtos = Produto.objects.filter(id__in=list(produtos_carro.values_list('produto_id', flat=True)))
    for produto in produtos:
        produto.vendido = True
        produto.save()
    carro = Carro.objects.all()
    carro.delete()
    return redirect('listagem')
