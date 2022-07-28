from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.contrib import messages


class Pagar(View):
    template_name = 'pedido/pagar.html'

    def get(self, *args, **kwargs):

        contexto = {}

        return render(self.request, self.template_name, contexto)


class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('FecharPedido')


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
