from django.urls import path
from loja import views

urlpatterns = [
    path('listagem/', views.listagem, name='listagem'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('detalhes', views.detalhes, name='detalhes')
]