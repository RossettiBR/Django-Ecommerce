from django.contrib import admin
from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


class ProtudoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'descricao_curta', 'get_preco_formatado', \
         'get_preco_promocional_formatado',
    list_display_links = 'nome', 'descricao_curta',
    inlines = [
        VariacaoInline
    ]


admin.site.register(Produto, ProtudoAdmin)
admin.site.register(Variacao)
