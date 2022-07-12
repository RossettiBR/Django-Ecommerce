from django.http import  HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import Produto


class ListaProdutos(ListView):
    model = Produto
    template_name = 'produto/lista.html'


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe Produto')


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar ao Carrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover do Carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
