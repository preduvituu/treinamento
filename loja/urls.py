from django.contrib.auth.decorators import login_required
from django.urls import path
from loja.views import (
    listagem, cadastroCategoria, cadastroProduto, carrinho, detalhes, comprarCarrinho
)


urlpatterns = [
    path('', login_required(listagem), name='listagem'),
    path('nova/categoria/', login_required(cadastroCategoria), name='cadastro_categoria'),
    path('novo/produto/', login_required(cadastroProduto), name='cadastro_produto'),
    path('detalhe/<int:pk>/', login_required(detalhes), name='detalhes'),
    path('carrinho/<int:pk_produto>/', login_required(carrinho), name='carrinho'),
    path('camprar/carrinho/', login_required(comprarCarrinho), name='comprar_carrinho')
]
