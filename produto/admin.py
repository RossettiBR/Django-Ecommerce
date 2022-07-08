from django.contrib import admin
from .models import Produto


class ProtudoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'preco_marketing', \
        'preco_marketing_promocional', 'tipo',
    list_display_links = 'id', 'nome',


admin.site.register(Produto, ProtudoAdmin)
