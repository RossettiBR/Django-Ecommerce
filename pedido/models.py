
from django.db import models
from django.contrib.auth.models import User

"""Pedido:
        user - FK User
        total - Float
        status - Choices
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),

"""


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return self.usuario


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.IntegerField()
    variacao = models.CharField(max_length=255, verbose_name='Variação')
    variacao_id = models.PositiveIntegerField(verbose_name='Variação id')
    preco = models.FloatField(verbose_name='Preço')
    preco_promocional = models.FloatField(default=0, verbose_name='Preço promocional')
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return self.pedido

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
