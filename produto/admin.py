from django.contrib import admin
from .models import Produto


class ProtudoAdmin(admin.ModelAdmin):
    ...

admin.site.register(Produto)