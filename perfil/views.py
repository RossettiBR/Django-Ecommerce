from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from . import models
from .forms import UserForm, PerfilForm


class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.contexto = {
            'uniform': UserForm(data=self.request.POST or None),
            'perfilform': PerfilForm(data=self.request.POST or None),
        }

        self.renderizar = render(
            self.request,
            self.template_name,
            contexto
        )

    def get(self, *args, **kwargs):
        return self.get(*args, **kwargs)


class Criar(BasePerfil):
    pass


class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')
