from django.urls import path
from loja import views

urlpatterns = [
    path('', views.listagem, name='listagem'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),
    path('cadastro_categoria/', views.cadastro_categoria, name='cadastro_categoria'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('<int:produto_id>', views.detalhes, name='detalhes')
]